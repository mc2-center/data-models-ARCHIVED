# Preliminaries
import pandas as pd
import argparse
import synapseclient
from synapseclient import Table
from data_model_attribute_dict import DM_KEY
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

    return cv_df


### Create dictionary of cv data frame
def controlled_vocab_dict(cv_df, data_model_dict):

    # Create new data frame, changing column names.
    cv_partial_df = cv_df[['attribute', 'preferredTerm']].copy()

    # Double check all attributes in original cv are represented in the data model, if not they may be deprecated and will need to be removed.
    updated_keys = attribute_check(cv_partial_df, data_model_dict)
    cv_partial_df = cv_partial_df[cv_partial_df['attribute'].isin(
        updated_keys)]

    # Create dictionary with attributes as keys and cv terms as a list of values
    cv_partial_df = cv_partial_df.groupby(['attribute'], as_index=False).agg(
        {'preferredTerm': lambda x: x.dropna().tolist()})
    cv_dict = dict(
        zip(cv_partial_df['attribute'], cv_partial_df['preferredTerm']))

    return (cv_dict)


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
            f"\n\nThere are attributes in the data model that use the same valid values, but do not match. Check that valid values are the same and update them in the data model csv so they match and rerun this script. Check attributes (see DM_KEY dictionary in data_model_attribute_dict.py) that use the valid values for:\n\n{data_model_df.loc[duplicate_attribute]}"
        )
        exit()
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


# Function to double check depecrated keys/attributes
def attribute_check(compare_df, data_model_dict):

    cv_keys = compare_df['attribute'].unique().tolist()
    updated_keys = []
    for attribute in cv_keys:
        if attribute not in data_model_dict.keys():
            # if attribute not in data model attributes
            choice = input(
                f"\n\nThe attribute '{attribute}' appears to not have valid values in the data model. It will be deleted from the controlled vocabulary. Continue on and delete from CV? Type 'y' for yes, or 'n' for No."
            )

            if choice == 'y':
                print(
                    f"\n\nDeleteing {attribute} as an attribute from new controlled vocabulary...."
                )
                continue
            elif choice == 'n':
                print(f"\n\nAdd '{attribute}' to data model and rerun script")
                exit()
            else:
                print(
                    "\n\nNot a valid input... Rerun and try inputting 'y' or 'n'"
                )
                exit()

        else:
            updated_keys.append(attribute)

    return updated_keys


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

    # Find capital versions of missing terms and corresponding attribute versions of missing terms and print output.
    if bool(dm_add) == True:
        for k, v in dm_add.items():
            cap_terms = []
            for item in v:
                cap_values = cv_dict.get(k)
                for term in cap_values:
                    if term.lower() == item:
                        cap_terms.append(term)
            attribute_list = []
            for key, value in DM_KEY.items():
                if k == value in DM_KEY.values():
                    attribute_list.append(key)
            print(
                f"\n\nPlease add {cap_terms} as valid value(s) to the data model (or edit in the current cv) for the attribute(s) {attribute_list} and rerun this script to update the CV."
            )
        exit()

    # Find capital version of missing terms. These should be missing terms from the CV. Mismatch should equal CV missing terms list after dm_add is empty
    else:
        for key, value in mismatch.items():
            missing = []
            for item in value:
                cap_values = dm_dict.get(key)
                for term in cap_values:
                    if term.lower() == item:
                        missing.append(term)
            print(f"\n\nMissing {key}:\n\n{missing}")

    # Can print cv or dm dictionaries here to check attributes missing from the controlled vocabulary
    # or attributes missing from the data model. Uncomment below as necessary. If there are terms missing from the dm, script should terminate.
    # cv dictionary should match mismatch dictionary after dm is empty.
    # print(f"\n\nTerms missing from data model: {dm}")
    # print(f"\n\nterms missing from controlled vocabulary {cv}")

    choice = input(
        "\n\nPlease double check missing values listed above, do any of the missing values need to be edited in the data model or controlled vocabulary before moving forward? Otherwise, they will be added to the updated controlled vocabulary. e.g. delete leading or trailing white spaces in values, etc. Type 's' to stop and make edits, type 'c' to continue with updating new controlled vocabulary"
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

    # Will combine duplicated terms (if they are exactly the same across all columns, except nonpreferredTerms, where it will create a list of nonpreferredTerms)
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

    # Create separate data frame for all values that are duplicated if they are not the same across all rows.
    duplicated_terms = term_details_df[term_details_df[[
        'attribute', 'preferredTerm', 'nonpreferredTerms', 'description',
        'ontologyIdentifier', 'ontologySource', 'ontologyUrl', 'notes'
    ]].duplicated(['attribute', 'preferredTerm'])]

    if duplicated_terms.empty:

        print("\n\nThere are no duplicated terms. CV Looks good...")

    else:

        print(f"\n\nDuplicated Terms: {duplicated_terms}")

        print(
            "\n\nPlease check duplicated terms listed above in current CV and fix so they may be combined. I.e make sure all columns match in the current CV for the same term with the exception of the Nonpreferred Terms column. Rerun script after fixing."
        )
        exit()

    # Option to save term_details as csv to check for errors. This csv will likely be the exact same as the final_df unless
    # there were multiple rows for one term, with different nonpreferredTerms (How we used to format the CV).
    # Uncomment below if desired.
    # term_details_df.to_csv('term_details_df.csv', index=False)

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
    final_df.to_csv('controlled_vocabulary.csv', index=False)

    print(f'\n\nFinal DF saved as CSV - called controlled_vocabulary.csv!')

    return final_df


# Function to map data types to columns to correctly match Synapse Schema
def col_data_type(syn, cv_table_id, final_df):

    cols = syn.getTableColumns(cv_table_id)

    col_dict = {}
    for col in cols:
        for k, v in col.items():
            if k == 'name':
                col_dict[v] = col['columnType']

    # Create dictionary to map Synapse data types to pandas data types
    data_type_dict = {
        'STRING': str,
        'INTEGER': int,
        'STRING_LIST': str,
        'LARGETEXT': str,
        'LINK': str,
        'BOOLEAN': bool,
        'USERID': str,
        'DOUBLE': float
    }

    # Map pandas/synapse data types to cv column names dictionary
    col_types_dict = {k: data_type_dict.get(v, v) for k, v in col_dict.items()}

    # Adjust final df data types to make sure they match Synapse CV table schema
    for k, v in col_types_dict.items():
        final_df[k] = final_df[k].astype(v)

    return (final_df)


# update and upload CV table in Synapse.
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
    cv_dictionary = controlled_vocab_dict(cv_df, data_model_dictionary)
    compare_dicts(cv_dictionary, data_model_dictionary)
    final_dict = merge_dicts(cv_dictionary, data_model_dictionary)
    updated_cv = final_df(final_dict, cv_df)
    final_cv = col_data_type(syn, args.table_id, updated_cv)

    choice = input(
        '\n\nDid you create a snapshot/version of the current CV in Synapse before proceeding with upload? Type "y" to continue with upload, type "n" to stop.'
    )

    if choice == 'y':
        update_cv_table(syn, args.table_id, final_cv)

    elif choice == 'n':
        print(
            '\n\nPlease create a snapshot/version of current CV table in synapse before proceeding with upload of updated CV and rerun script.'
        )

        exit()

    else:
        print("\n\nNot a valid input.")

        main()


if __name__ == "__main__":
    main()