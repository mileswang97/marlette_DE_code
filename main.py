"""
This is the entrypoint to the program. 'python main.py' will be executed and the 
expected csv file should exist in ../data/destination/ after the execution is complete.
"""
# PSL
import argparse
import sys
# self-defined modules
from utils import test

if __name__ == '__main__':
    """Entrypoint"""
    print('Beginning the ETL process...')
    parser = argparse.ArgumentParser()
    parser.add_argument("delim")
    args = parser.parse_args()
    delimiter = args.delim
    #test()