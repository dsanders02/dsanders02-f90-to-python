#!/usr/bin/env python3
import sys

num_lines = 0
total_size  = 0 
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    count, size = line.split(maxsplit=1)
    total_size += int(count) * int(size)
    num_lines += 1 
    print(count, size)
print(num_lines, total_size)
