#!/usr/bin/env python

#gunzip bowtie2.sam.gz ran this in command line

# import gzip
# f=gzip.open('bowtie2.sam','rb')
# file_content=f.read()
# print(file_content)

with open ("bowtie2.sam", 'r') as bf:
    for line in bf:
        line = line.rstrip()
        print(line)

    #tab seperated
