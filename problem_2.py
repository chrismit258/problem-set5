#! /usr/bin/env python3

import sys
from collections import Counter

filename = sys.argv[1]

count = 0

bases = Counter()

for line in open('/vol2/home/smithc/data-sets/fastq/SP1.fq'):
    line = line.rstrip()
    if count == 0:
        name = line
        count += 1

    elif count == 1:
        seq = line
        count += 1

    elif count == 2:
        count += 1

    elif count == 3: 
        qual = line
        count = 0

        for base in seq: 
            bases[base] += 1

print(bases['C'])
