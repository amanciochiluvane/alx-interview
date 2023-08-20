#!/usr/bin/python3

import sys
import signal

def print_statistics(total_file_size, status_code_counts):
    """
    Print statistics including total file size and status code counts.
    Args:
        total_file_size (int): Total accumulated file size.
        status_code_counts (dict): Dictionary of status codes and their counts.
    Returns:
        None
    """
    print("Total file size:", total_file_size)
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")

def signal_handler(sig, frame):
    """
    Signal handler to print statistics upon interruption (CTRL + C).
    Args:
        sig: Signal number.
        frame: Current stack frame.
    Returns:
        None
    """
    print_statistics(total_size, status_code_counts)
    sys.exit(0)

total_size = 0
status_code_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
line_count = 0

signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        parts = line.strip().split()
        if len(parts) != 10:
            continue

        _, _, _, _, _, _, status_code, file_size = parts
        try:
            status_code = int(status_code)
            file_size = int(file_size)
        except ValueError:
            continue

        total_size += file_size
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1

        line_count += 1
        if line_count % 10 == 0:
            print_statistics(total_size, status_code_counts)
            line_count = 0

except KeyboardInterrupt:
    print_statistics(total_size, status_code_counts)

