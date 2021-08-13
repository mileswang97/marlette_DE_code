# PSL
import datetime
import csv

## GRABBING AND WRITING DATA

# return list of lines, stripped and split
def get_source_data(filepath, delimiter) -> list:
    if delimiter is None:
        # default delimiter
        delimiter = '|'
    temp_list = list()
    with open(filepath, 'r') as f:
        lines = f.readlines()
        for line in lines:
            split = line.strip().split(delimiter)
            temp_list.append(split)
    return temp_list

def sort_header(header_list) -> list:
    sorted_header = sorted(header_list, key=lambda obj: int(obj[0]))
    sorted_headers_list = [obj[1] for obj in sorted_header]
    return sorted_headers_list

def write_to_csv(obj_list, header, filepath) -> None:
    with open(filepath, 'w') as f:
        csv_writer = csv.writer(f, delimiter=',')
        csv_writer.writerow(header)
        for row in obj_list:
            csv_writer.writerow(row)
    return

## ERROR CHECKING

def append_log(message, filepath='log.txt') -> None:
    with open(filepath, 'a') as f:
        f.write(message)
    return

def find_date_index(sorted_headers_list) -> list:
    return ['Date' in obj for obj in sorted_headers_list]

def find_time_index(sorted_headers_list) -> list:
    return ['Time' in obj for obj in sorted_headers_list]

def validate_date(str) -> bool:
    try:
        datetime.datetime.strptime(str, "%Y-%m-%d")
        return True
    except:
        return False

def validate_time(str) -> bool:
    try:
        datetime.datetime.strptime(str, "%H:%M:%S")
        return True
    except:
        return False

def error_check(obj_list, date_index_list, time_index_list) -> list:
    append_log(f'RUNNING {datetime.datetime.today()}\n')
    removal_list = list()
    for obj in obj_list:
        validation_list = list()
        for index in range(len(obj)):
            if date_index_list[index]:
                validation_list.append(validate_date(obj[index]))
            if time_index_list[index]:
                validation_list.append(validate_time(obj[index]))
        if False in validation_list:
            removal_list.append(obj)        
    for obj_remove in removal_list:
        append_log(f'Line {obj_remove} has been removed.\n')
        obj_list.remove(obj_remove)
    return obj_list