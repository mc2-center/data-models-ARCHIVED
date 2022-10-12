# Preliminaries
import pandas as pd
import argparse
import synapseclient
from synapseclient import Table
from data_model_attribute_dict import DM_KEY, CV_KEY
import numpy as np
from sys import exit
import numpy as np


### Login to Synapse ###
def login():

    syn = synapseclient.Synapse()
    syn.login()

    return syn


### Get arguments ###
def get_args():

    parser = argparse.ArgumentParser(
        description='Get synapse cv table id and data model file path')
    parser.add_argument('table_id',
                        type=str,
                        help='Synapse controlled vocabulary table id')
    parser.add_argument('file_path',
                        type=str,
                        help='File path where data model csv is stored')

    return parser.parse_args()


### Retrieve CV table and turn into data frame ###
def get_cv(syn, table):

    cv_query = (f"SELECT * FROM {table}")
    cv_df = syn.tableQuery(cv_query).asDataFrame()

    # Convert nonpreferredTerms to string from stringList
    cv_df['nonpreferredTerms'] = cv_df['nonpreferredTerms'].map(str).replace(
        '[None]', '').str.strip("[|]|'").replace(r'^\s*$', np.nan, regex=True)

    cv_df = cv_df.replace({
        'attribute': CV_KEY,
    }).dropna(how='all')

    return cv_df


### Create dictionary of cv data frame
def controlled_vocab_dict(cv_df):

    # Create new data frame, changing column names.
    cv_partial_df = cv_df[['attribute', 'preferredTerm']].copy()

    # Double check all attributes in original cv are represented in CV_KEY dict, if not they may be deprecated and will need to be removed.
    updated_keys = attribute_check(cv_partial_df)
    cv_partial_df = cv_partial_df[cv_partial_df['attribute'].isin(
        updated_keys)]

    # Create dictionary with attributes as keys and cv terms as a list of values
    cv_partial_df = cv_partial_df.groupby(['attribute'], as_index=False).agg(
        {'preferredTerm': lambda x: x.dropna().tolist()})
    cv_dict = dict(
        zip(cv_partial_df['attribute'], cv_partial_df['preferredTerm']))

    return (cv_dict)


# Function to double check depecrated keys/attributes
def attribute_check(compare_df):
    cv_keys = compare_df['attribute'].unique().tolist()
    updated_keys = []
    for attribute in cv_keys:
        if attribute not in CV_KEY.values():
            choice = input(
                f"\n\nThe attribute '{attribute}' is not in the data model. It will be deleted from the controlled vocabulary. Continue on? Type 'y' for yes, or 'n' for No."
            )

            if choice == 'y':
                print(
                    f"\n\ndeleteing {attribute} as an attribute from new controlled vocabulary...."
                )
                continue
            elif choice == 'n':
                print(f"\n\nAdd '{attribute}'' to data model and rerun script")
                exit()
            else:
                print(
                    "\n\nNot a valid input... Rerun and try inputting 'y' or 'n'"
                )
                exit()

        else:
            updated_keys.append(attribute)

    return updated_keys


# Create a dictionary from the data model valid values
def data_model_dict(file_path):

    data_model_df = pd.read_csv(file_path)
    data_model_df = data_model_df.filter(
        items=['Attribute', 'Valid Values']).dropna().rename(
            columns={
                'Attribute': 'attribute',
                'Valid Values': 'preferredTerm'
            })

    # Replace Attribute names according to dictionary and drop duplicates
    data_model_df = data_model_df.replace({
        'attribute': DM_KEY
    }).drop_duplicates(subset=['attribute', 'preferredTerm'], keep='first')

    # If any attributes duplicated, check valid values and how they differ
    duplicate_attribute = data_model_df.duplicated(subset=['attribute'])
    if duplicate_attribute.any():
        print(
            f"\n\nThere is a duplicated attribute, check that valid values are the same for: {data_model_df.loc[duplicate_attribute]}"
        )
    else:
        print("\n\nAttributes updated for data model cv data frame")

        # Convert valid values to lists using a dictionary so we can iterate
        data_model_df['preferredTerm'] = data_model_df['preferredTerm'].astype(
            'string')
        data_model_dict = dict(
            zip(data_model_df['attribute'], data_model_df['preferredTerm']))
        for key in data_model_dict.keys():
            data_model_dict[key] = data_model_dict[key].split(", ")

        return data_model_dict


# Compare valid values for controlled vocabulary and data model, qc differences, and merge
def compare_dicts(cv_dict, dm_dict):

    # Convert dictionaries to lower case to ignore casing.
    cv_dict_lower = dict(cv_dict)
    dm_dict_lower = dict(dm_dict)
    for key, value in cv_dict_lower.items():
        cv_dict_lower[key] = [x.lower() for x in value]
    for key, value in dm_dict_lower.items():
        dm_dict_lower[key] = [x.lower() for x in value]

    # Compare dictionaries
    mismatch = {}
    cv = {}
    dm = {}

    for attribute in list(
            set([attribute for attribute in cv_dict_lower] +
                [attribute for attribute in dm_dict_lower])):
        set_cv = set(cv_dict_lower.get(attribute, []))
        set_dm = set(dm_dict_lower.get(attribute, []))
        mismatch[attribute] = list(
            set_cv.union(set_dm) - set_cv.intersection(set_dm))
        cv[attribute] = list(set_dm - set_cv)
        dm[attribute] = list(set_cv - set_dm)

    # Create dictionary of values missing in the data model that will need to be added to the data model before moving forward.
    dm_add = {}
    for k, v in dm.items():
        if len(v) != 0:
            dm_add[k] = v

    if bool(dm_add) == True:
        for k, v in dm_add.items():
            attribute_list = []
            for key, value in DM_KEY.items():
                if k == value in DM_KEY.values():
                    attribute_list.append(key)
            print(
                f"Please add {v} as valid value(s) to the data model (or edit in the current cv) for the attribute(s) {attribute_list} and rerun this script to update the CV."
            )
        exit()

    else:
        for key, value in mismatch.items():
            missing = []
            for item in value:
                missing.append(item)
            print(f"\n\nMissing {key}:\n\n{missing}")

    # Can print cv or dm dictionaries here to check attributes missing from the controlled vocabulary
    # or attributes missing from the data model. Uncomment below as necessary. If there are terms missing from the dm, script should terminate.
    # cv dictionary should match mismatch dictionary after dm is empty.
    # print(f"\n\nTerms missing from data model: {dm}")
    # print(f"terms missing from controlled vocabulary {cv}")

    choice = input(
        "\n\nPlease double check missing values listed above, do any of the missing values need to be edited in the data model or controlled vocabulary before moving forward? Otherwise, they will be added to the updated controlled vocabulary. e.g. delete leading or trailing white spaces in values, etc. Note all terms are shown in lowercase, but will be changed. Type 's' to stop and make edits, type 'c' to continue with updating new controlled vocabulary"
    )

    if choice == 's':

        print(
            "\n\nEdit the values in the controlled vocabulary or data model and rerun script"
        )
        exit()

    elif choice == 'c':

        print("\n\nMoving on...\n\n")
        return mismatch

    else:

        print(
            "\n\nNot a valid input... Rerun and try inputting 's' for stop or 'c' for continue"
        )
        exit()


def merge_dicts(cv_dict, dm_dict):

    final_dict = cv_dict | dm_dict

    return final_dict


def final_df(final_dict, cv_df):

    final_df = pd.DataFrame(final_dict.items(),
                            columns=['attribute', 'preferredTerm'])

    final_df = final_df.explode('preferredTerm')

    term_details_df = cv_df.groupby([
        'attribute', 'preferredTerm', 'description', 'ontologyIdentifier',
        'ontologySource', 'ontologyUrl', 'notes'
    ],
                                    dropna=False,
                                    as_index=False).agg({
                                        'nonpreferredTerms':
                                        lambda x: x.dropna().tolist()
                                    })

    # Drop empty rows
    term_details_df = term_details_df[term_details_df['preferredTerm'].notna()]

    # Create separate data frame for all values that are duplicated
    duplicated_terms = term_details_df[term_details_df[[
        'attribute', 'preferredTerm', 'nonpreferredTerms', 'description',
        'ontologyIdentifier', 'ontologySource', 'ontologyUrl', 'notes'
    ]].duplicated(['attribute', 'preferredTerm'])]

    if duplicated_terms.empty:

        print("\n\nThere are no duplicated terms. CV Looks good...")

    else:

        print(f"\n\nDuplicated Terms: {duplicated_terms}")

        print(
            "\n\n Please check duplicated terms listed above in current CV and fix so they may be combined. I.e make sure all columns match in the current CV for the same term with the exception of the Nonpreferred Terms column. Rerun script after fixing."
        )
        exit()

    #  Add terms where first letter is capitlized to nonpreferred terms to account for changes
    #  in annotations (this will help change legacy annotations where capitalization was changed in the valid values of the data model)
    for i, r in term_details_df.iterrows():
        cap_term = r['preferredTerm'].capitalize()
        term_list = r['nonpreferredTerms']
        if cap_term not in term_list:
            term_list.append(cap_term)
        if r['preferredTerm'] == cap_term:
            term_list.remove(cap_term)

    term_details_df.to_csv('term_details_df.csv', index=False)

    final_df = final_df.merge(term_details_df[[
        'attribute', 'preferredTerm', 'nonpreferredTerms', 'description',
        'ontologyIdentifier', 'ontologySource', 'ontologyUrl', 'notes'
    ]],
                              on=['attribute', 'preferredTerm'],
                              how='left')

    # Change order of columns and sort
    final_df = final_df[[
        'attribute', 'preferredTerm', 'nonpreferredTerms', 'description',
        'ontologySource', 'ontologyIdentifier', 'ontologyUrl', 'notes'
    ]].sort_values(by=['attribute', 'preferredTerm']).fillna('')

    # Save final df as csv in case something goes wrong with table upload.
    final_df.to_csv('final_vocabulary.csv', index=False)

    return final_df


# update columns in current cv table in Synapse to match new CV column names
def update_cv_table(syn, table_id, final_df):

    # Delete all rows in current table
    current_rows = syn.tableQuery(f"SELECT * FROM {table_id}")
    syn.delete(current_rows)

    # Store updated cv
    syn.store(Table(table_id, final_df))

    print(
        "\n\n Controlled Vocabulary Table succcessfully updated and uploaded to Synapse!!"
    )


def main():

    syn = login()
    args = get_args()
    cv_df = get_cv(syn, args.table_id)
    data_model_dictionary = data_model_dict(args.file_path)
    cv_dictionary = controlled_vocab_dict(cv_df)
    compare_dicts(cv_dictionary, data_model_dictionary)
    final_dict = merge_dicts(cv_dictionary, data_model_dictionary)
    updated_cv = final_df(final_dict, cv_df)
    update_cv_table(syn, args.table_id, updated_cv)


if __name__ == "__main__":
    main()