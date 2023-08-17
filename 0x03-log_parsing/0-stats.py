#!/usr/bin/python3

import sys

total_file_size = 0
status_code_count = {}

def print_statistics():
    print("Total file size:", total_file_size)
    sorted_status_codes = sorted(status_code_count.keys())
    for code in sorted_status_codes:
        print(f"{code}: {status_code_count[code]}")

try:
    line_number = 0
    for line in sys.stdin:
        line_number += 1
        line = line.strip()

        parts = line.split()
        if len(parts) != 10:
            continue

        ip_address = parts[0]
        date = parts[2][1:]  # Removing '[' from the date
        status_code = parts[8]
        try:
            status_code = int(status_code)
        except ValueError:
            continue

        file_size = int(parts[9])
        total_file_size += file_size

        if status_code in status_code_count:
            status_code_count[status_code] += 1
        else:
            status_code_count[status_code] = 1

        if line_number % 10 == 0:
            print_statistics()

except KeyboardInterrupt:
    print_statistics()
