#!/usr/bin/env python3

from Bio import SeqIO

#Question 1:
record_list = [] 
record_list = list(SeqIO.parse("Python_08.fasta", "fasta"))
# print(len(record_list))

complete_nucleotide_len = 0

list_sequence_length = []

for seq_record in SeqIO.parse("Python_08.fasta", "fasta"): #echo "$PWD/Python_08.fasta" or "pwd" and add document
    
    fasta_name = seq_record.name
    fasta_id = seq_record.id
    fasta_description = seq_record.description
    fasta_sequence = seq_record.seq

    list_sequence_length.append(str(fasta_sequence))
    list_sequence_length.sort(key = len)

# for seq in list_sequence_length: #to print out the sequence length in list (list_sequence_length) to control if the sort method worked
#     print(len(seq))
print(len(list_sequence_length[0]))
print(len(list_sequence_length[-1])) # reverse [::-1] and get last value [-1]
    # print ("Name" , fasta_name , "\t")
    # print("ID" , fasta_id , "\t")
    # print( "Description" , fasta_description , "\t" )
    # print( "Sequence" , fasta_sequence , "\t" )

#     complete_nucleotide_len += len(fasta_sequence)
# print(complete_nucleotide_len)


# average_seq_length = complete_nucleotide_len/len(record_list)
# print(average_seq_length)
        

