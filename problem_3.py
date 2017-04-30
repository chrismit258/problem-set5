#! /usr/bin/env python3 

import sys
from collections import Counter

filename = sys.argv[1]

count = 0
aka_hexamers_5 = Counter()
aka_hexamers_3 = Counter()

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

    elif count ==3: 
        qual = line
        count = 0

        hexamer_5 = []
        hexamer_3 = []
        aka_hexamer_5 = seq[0:6]
        aka_hexamer_3 = seq[-6:]
        aka_hexamers_5[aka_hexamer_5] += 1
        aka_hexamers_3[aka_hexamer_3] += 1

for key, value in aka_hexamers_5.items():
    sortme = [(v,k) for k,v in aka_hexamers_5.items()]
    sortme
    sortme.sort()
    sortme.reverse()
print("The most common 5' hexamer is", sortme[0][1])

for key, value in aka_hexamers_3.items():
    sortme = [(v,k) for k,v in aka_hexamers_3.items()]
    sortme
    sortme.sort()
    sortme.reverse()
print("The most common 3' hexamer is", sortme[0][1])

