#!/usr/bin/env python3

#Problemset 10

#Question 1:

# dna = 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCT'


# def reformated_dna_sequence(dna): #def makes it a function. it is followed by an indentation
#     complete_dna = "" # I have to define it as local (inside function), not outside (global)
#     for i in range (0, len(dna), 60):   #this iterates i in the range from 0 to end of the sequence (= length of the sequence), im 60x i intervalls
#                                         #this means it shows (0, 60, 120 if you print it...) It is usually a good idea to 
#         sub_dna = dna[i : i+60] + "\n"  # sub_dna is a section of the dna sequence which is defined by the markers given in []
#                                         #it basically says that it is takes the distance starting at i (which uses intervall of 60 steps with every single loop run)
#                                         # and adds a new line (\n) at the end of it
#         complete_dna += sub_dna         #sub_dna saves everything as a substring - to save everything in one continoous string you need to concatenate it
#     return complete_dna                 #return ends a functions and returns the complete merged dna - here no () is needed, otherwise it is a tuple
    
# print (reformated_dna_sequence(dna))

# or alternative way of printing it:
# run_complete_function = reformated_dna_sequence(dna)
# print(run_complete_function)

# other options include: regular expression or creating a list and adding each sub_dna into it (analogous to complete_dna += sub_dna, but using a list)
# for the list you need to join it in the end.

# it is important that there is a complete string as the sub_dna are substrings

#append is a list function
# += is a universal way of adding up


#Question 2:

dna = '''GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACC
GTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACG
CTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCC
TCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAA
TGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATG
CCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCT
GTCATCTTCT'''

def reformated_dna_sequence(dna): 
    complete_dna = "" 
    
    for line in dna:                                  
        line_rstrip = line.rstrip()                
        complete_dna += line_rstrip       
    return complete_dna                
    
print (reformated_dna_sequence(dna))

# in this example - the \n will be removed by using rstrip(), which removes \n on the right hand side
# the difference here is to make sure that you iterate through all lines, as different from question 1, 
# where we iterated through the characters with range 