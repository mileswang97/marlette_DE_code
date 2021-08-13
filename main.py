"""
This is the entrypoint to the program. 'python main.py' will be executed and the 
expected csv file should exist in ../data/destination/ after the execution is complete.
"""
# PSL
import argparse
import os
# self-defined modules
from utils import (
    get_source_data, 
    sort_header, 
    write_to_csv, 
    find_date_index, 
    find_time_index, 
    error_check,
)
from src.some_storage_library import SomeStorageLibrary

if __name__ == '__main__':
    """Entrypoint"""
    print('Beginning the ETL process...')
    
    # add optional argument for changing delimiter, in case its not pipe
    parser = argparse.ArgumentParser()
    parser.add_argument("-d")
    args = parser.parse_args()
    delimiter = args.d

    # define filepaths
    sourcecolumnsfp = os.path.join(os.getcwd(), 'data', 'source', 'SOURCECOLUMNS.txt')
    sourcedatafp = os.path.join(os.getcwd(), 'data', 'source', 'SOURCEDATA.txt')
    sourceresultfp = 'result.csv'

    # get data
    source_headers = get_source_data(sourcecolumnsfp, delimiter)
    source_data = get_source_data(sourcedatafp, delimiter)
    sorted_headers_list = sort_header(source_headers)

    # error check data, log errors
    # I suspect this wasn't part of the assignment given how many lines were removed, 
    # But I would want this in practice (less data is better than faulty data!)
    date_index_list = find_date_index(sorted_headers_list)
    time_index_list = find_time_index(sorted_headers_list)
    final_data = error_check(source_data, date_index_list, time_index_list)

    # write csv and move to directory
    write_to_csv(final_data, sorted_headers_list, sourceresultfp)
    SomeStorageLibrary().load_csv(sourceresultfp)