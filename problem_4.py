#! /usr/bin/env python3

import sys
from collections import Counter

filename = sys.argv[1]

from pysam import AlignmentFile
bamfile = AlignmentFile('/vol2/home/smithc/data-sets/bam/myc.hela.chr22.bam')

strand = []
mismatches = []
for record in bamfile: 
    strand.append(record.flag)
    mismatches.append(record.get_tag('NM'))

strand_count = Counter(strand)
mismatches_count = Counter(mismatches)

sortme = [(v,k) for k,v in strand_count.items()]
print(sortme)

print("Total alignments on the neg strand (16):", sortme[0][0])

print("Total alignments on the pos strand (0):", sortme[1][0])

sortme = [(v,k) for k,v in mismatches_count.items()]
print(sortme)

print("Alignments with no mismatches:", sortme[0][0])

a = sortme[1][0]
b = sortme[2][0]
c = sortme[3][0]
d = sortme[4][0]

alignments = [a, b, c, d]
total = sum(alignments)
print("Alignments with more than 0 mismatches:", total)






