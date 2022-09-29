""""Script to generate comma separated list of valid values to be paseted into data model csv"""

import synapseclient
import argparse


### Login to Synapse ###
def login():

    syn = synapseclient.Synapse()
    syn.login()

    return syn


### Get arguments ###
def get_args():

    parser = argparse.ArgumentParser(
        description=
        'Get synapse table id and column name for list of valid values to be generated from'
    )
    parser.add_argument(
        'table_id',
        type=str,
        help=
        'Synapse table id where valid values will be taken from. Only use normalized tables!'
    )
    parser.add_argument(
        'column_name',
        type=str,
        help='Synapse column name where valid values will be taken from')

    return parser.parse_args()


# Query table and generate a comma separated list that can be copied and pasted into corresponding valid values of data model.
def generate_list(table_id, column_name, syn):

    query = (f"SELECT {column_name} FROM {table_id}")
    df = syn.tableQuery(query).asDataFrame()
    the_list = df[column_name].values.tolist()
    comma_separated_list = ", ".join(the_list)

    list_print = print(
        f"\n\nComma separated list for {column_name} attribute:\n\n\n{comma_separated_list}"
    )

    return list_print


def main():

    syn = login()
    args = get_args()
    final_list = generate_list(args.table_id, args.column_name, syn)

    print(
        f"\n\nPlease copy the above list and paste into the valid values of the data model csv for the {args.column_name} attribute."
    )


if __name__ == "__main__":
    main()