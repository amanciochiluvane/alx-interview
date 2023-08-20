#!/usr/bin/python3

import sys

def print_msg(dict_sc, total_file_size):
    """
    Method to print
    Args:
        dict_sc: dict of status codes
        total_file_size: total of the file
    Returns:
        Nothing
    """
    print("File size: {}".format(total_file_size))
    for key, val in sorted(dict_sc.items()):
        if val != 0:
            print("{}: {}".format(key, val))

total_file_size = 0
code = 0
counter = 0
dict_sc = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

try:
    for line in sys.stdin:
        parsed_line = line.strip().split()  # Split the line into parts
        if len(parsed_line) == 10:  # Check if the line has the correct format
            counter += 1

            total_file_size += int(parsed_line[-1])  # File size is the last element
            code = parsed_line[-2]  # Status code is the second-to-last element

            if code in dict_sc:
                dict_sc[code] += 1

            if counter == 10:
                print_msg(dict_sc, total_file_size)
                counter = 0

finally:
    print_msg(dict_sc, total_file_size)
