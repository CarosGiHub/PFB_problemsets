#!/usr/bin/env python3

from Bio import SeqIO

# Question 1:
record_list = [] 
record_list = list(SeqIO.parse("Python_08.fasta", "fasta"))
# print(len(record_list))

# Question 2:

complete_nucleotide_len = 0 #you have to set it to 0 to start count the cummultive length in for loop

list_sequence_length = [] #initiate a list for sequence length to sort and print largest sequence 

for seq_record in SeqIO.parse("Python_08.fasta", "fasta"): #echo "$PWD/Python_08.fasta" or "pwd" and add document
    
    fasta_name = seq_record.name #use biopython to retieve information for .name, .id, .description, .seq
    fasta_id = seq_record.id
    fasta_description = seq_record.description
    fasta_sequence = seq_record.seq

    list_sequence_length.append(str(fasta_sequence)) #in the for loop each time it runs it appends the list of sequences
    list_sequence_length.sort(key = len) #those can now be sorted by length

# for seq in list_sequence_length: #to print out the sequence length in list (list_sequence_length) to control if the sort method worked
#     print(len(seq))
print(len(list_sequence_length[0]))
print(len(list_sequence_length[-1])) # reverse would be [::-1], to get last value [-1]
    # print ("Name" , fasta_name , "\t")
    # print("ID" , fasta_id , "\t")
    # print( "Description" , fasta_description , "\t" )
    # print( "Sequence" , fasta_sequence , "\t" )

#     complete_nucleotide_len += len(fasta_sequence)
# print(complete_nucleotide_len)


# average_seq_length = complete_nucleotide_len/len(record_list)
# print(average_seq_length)

# Use the BioSeqRecord.SeqRecord

from Bio.SeqUtils import gc_fraction
print(gc_fraction('GGCCTTTTTTTT'))


for seq_record in SeqIO.parse("Python_08.fasta", "fasta"): 
    print(seq_record.id , gc_fraction(seq_record))
    #you could also create a list to store this information in



#BLAST
# curl -OL ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_sprot.fasta.gz used in command line to
#download