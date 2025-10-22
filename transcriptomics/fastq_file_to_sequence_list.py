#!/usr/bin/env python

import os, sys

## method: seq_list_from_fastq_file(fastq_filename)
##
##  Extracts the sequence lines from a fastq file and returns a list
##  of the sequence lines
##
##  input parameters:
##
##  fastq_filename :  name of the fastq file (type: string)
##
##  returns seq_list : list of read sequences.
##                    ie.  ["GATCGCATAG", "CGATGCAG", ...]

from Bio import SeqIO

def seq_list_from_fastq_file(fastq_filename, num_seqs_show):

    print(f"running this function for {fastq_filename}")
    complete_list = []
    complete_list = list((SeqIO.parse(fastq_filename, "fastq")))
    # print(seq_list)
    
    seq_list = []
    for entry in complete_list:
        # print(entry)
        fastq_sequence = entry.seq
        # print(f"fastq_sequence is {fastq_sequence}")
        seq_list.append(str(fastq_sequence))
    #print(seq_list[:num_seqs_show])
    
    ## end your code

    return seq_list



def main():

    progname = sys.argv[0]
    
    usage = "\n\n\tusage: {} filename.fastq num_seqs_show\n\n\n".format(progname)
    
    if len(sys.argv) < 3:
        sys.stderr.write(usage)
        sys.exit(1)

    # capture command-line arguments
    fastq_filename = sys.argv[1]
    num_seqs_show = int(sys.argv[2])

    seq_list = seq_list_from_fastq_file(fastq_filename, num_seqs_show)

    print(seq_list[0:num_seqs_show])

    sys.exit(0)  # always good practice to indicate worked ok!



if __name__ == '__main__':
    main()
    
