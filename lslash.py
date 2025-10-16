#!/usr/bin/env python3
import sys
import re

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    date, size, permissions, grpid, owner, filepath = line.split()
    # yyyy/mm/dd       file size   permissions       grpid      owner /fully/resolved/pathname/filename
    match = re.search(r'[^/]+$', filepath) 
    if match:
        filename = match.group(0) # For the first two regex, group(0) gives the full match
    else:
       filename = 'Could not find filename'
    
    print(filename)
