#!/usr/bin/env python3

#Question1:
#This is a FASTA parser, that you can use to save sequences as values to a sequence ID.
#Remember FASTA is different from FASQ parser that worked with modulus


# import re

# fasta_dict = {}
# with open("Python_08.fasta.txt", "r") as seq_file:
#     # fasta_sample = seq_file.read()
#     for line in seq_file:
#         line = line.rstrip()
#         if re.search(r"(^>\w+)" , line):
#             for match in re.finditer(r"(^>\w+)" , line):
#                 gene_id = match.group(1) #calling out subpattern match. (^>\w+) is at index 1, r is index 0
#                 gene_id = gene_id.lstrip(">") # you need to do it here beacuse > is character
#                 # print(gene_id) #just needed for testing
#                 fasta_dict[gene_id] = "" #make a key  
#         else:
#             #print(line)
#             fasta_dict[gene_id] += line #adding value to key
#     print(fasta_dict)




# import re

# fasta_dict = {}
# with open("Python_08.fasta.txt", "r") as seq_file:
#     # fasta_sample = seq_file.read()
#     for line in seq_file:
#         line = line.rstrip()
#         if re.search(r"(^>\w+)" , line):
#             for match in re.finditer(r"(^>\w+)" , line):
#                 gene_id = match.group(1) 
#                 gene_id = gene_id.lstrip(">") 
#                 fasta_dict[gene_id] = "" 
#         else:
#             #print(line)
#             fasta_dict[gene_id] += line #adding value to key
#             nt_count = {} #create a new list that stores the count for each nucleotide
#             #for this I need to first define all characters that are unique in the sequence using the
#     print(fasta_dict)




#Question 1:

import re

fasta_dict = {}
with open("Python_08.fasta.txt", "r") as seq_file:
    # fasta_sample = seq_file.read()
    for line in seq_file:
        line = line.rstrip()
        match = re.search(r"(^>\w+)" , line)
        if match:
            #for match in re.finditer(r"(^>\w+)" , line): #to keep () around the ^>\w+ I want to find 
            gene_id = match.group(1) 
            gene_id = gene_id.lstrip(">")
            nt_count = {"A" : 0 , "C" : 0, "T" : 0 , "G": 0} #create a new list that stores the count for each nucleotide
            #for this I need to first define all characters that are unique in the sequence using the set function 
            fasta_dict[gene_id] = nt_count
            
        else:
            #print(line)
            # fasta_dict[gene_id] += line #adding value to key
            unique = set(line)
            print ("unique nt: ", unique)
            for nt in unique:
                count = line.count(nt)
                nt_count[nt] += count
    print(fasta_dict)
    print(nt_count)
