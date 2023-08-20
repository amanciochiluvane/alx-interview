#!/usr/bin/python3

import sys

# Initialize variables to store metrics
total_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
lines_processed = 0

try:
    for line in sys.stdin:
        line = line.strip()
        
        # Split the line into parts
        parts = line.split()
        if len(parts) != 10:
            continue
        
        # Extract relevant information from the line
        ip_address, _, _, _, _, request, status_code, file_size = parts[0], parts[5], parts[8], parts[9]
        
        # Check if status_code is a valid integer
        try:
            status_code = int(status_code)
        except ValueError:
            continue
        
        # Update metrics
        total_size += int(file_size)
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1
        
        lines_processed += 1
        
        # Print statistics every 10 lines
        if lines_processed % 10 == 0:
            print(f"Total file size: {total_size}")
            for code, count in sorted(status_code_counts.items()):
                if count > 0:
                    print(f"{code}: {count}")
        
except KeyboardInterrupt:
    # Print final statistics on keyboard interruption
    print(f"Total file size: {total_size}")
    for code, count in sorted(status_code_counts.items()):
        if count > 0:
            print(f"{code}: {count}")
