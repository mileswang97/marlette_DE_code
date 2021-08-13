# PSL
import datetime as dt
import os
import csv

class Order:
    def __init__(self):
        pass
    

# customize delimiter
delimiter = "|"

def test():
    print("testing")
    return

# return list of lines, stripped and split
def get_source_data(filepath, delimiter) -> list:
    temp_list = list()
    with open(filepath, 'r') as f:
        lines = f.readlines()
        for line in lines:
            split = line.strip().split(delimiter)
            temp_list.append(split)
    return temp_list

sourcecolumns = os.path.join(os.getcwd(), "data", "source", "SOURCECOLUMNS.txt")
sourcedata = os.path.join(os.getcwd(), "data", "source", "SOURCEDATA.txt")

print(get_source_data(sourcecolumns, "|"))

def write_to_open_csv(csv_writer, write_rows):
    for row in write_rows:
        csv_writer.writerow(row)

