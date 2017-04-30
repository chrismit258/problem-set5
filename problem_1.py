#! /usr/bin/env python3   


from collections import Counter

counts = Counter()
for line in open('/vol2/home/smithc/data-sets/bed/lamina.bed'):
    if line.startswith('#'): continue
    fields = line.split('\t')
    chrom = fields[0]
    counts[chrom] += 1
for chrom, count in counts.items():
    sortme = [(v,k) for k,v in counts.items()]
    sortme
    sortme.sort()
    sortme.reverse()
print(sortme[0][1])
