#!/usr/bin/env python3

# Question 1
# Save Document an be sure you are in the correct directory. Otherwise check ls in terminal, maybe move one up .. and see where document is located
# If you are in the right diretort choose "r" ro read document
# If you would like to modify a line - use iteration of this in for loop.

# songtext_file_object = open("Python_06.txt", "r")
# for line in songtext_file_object:
#     line = line.upper()
#     print(line)

# you could also use the following:
# with open("Python_06.txt", "r") as songtext_file_object:
#     for line in songtext_file_object:
#         line = line.upper()
#         print(line)

# Question 2:
# with open("Python_06.txt", "r") as sequence_read, open ("Python_06_uc.txt", "w") as sequence_write:
#     for line in sequence_read:
#         line = line.upper()
#         sequence_write.write(line)
#     sequence_write.write("/n") #this line is not necessarily needed as the text ends with an new line already. 
# if you want to make sure it has it - add the "/n". Also remember that there is a only one string allowed per write command.
# if you want to check what is printed in the document. Make sure you are in the right working directory - cat Python_6_uc.txt 
# and run it via the command line

# Question 3:
# Here one gets an text document with a line is the following format:  seqName\tsequence\n. They are seperated by tabs. 
# with open("Python_06.seq.txt", "r") as sequence_read:
#     for line in sequence_read:
#         list = line.split("\t")
#         reverse_sequence = list[1][::-1]
#         print(f"This is the reverse sequence {reverse_sequence}")
#
#Question 4:
# READ, CALCULATE, REPORT
with open("Python_06.fastq.txt", "r") as fastq_file:
    count_lines = 0
    number_characters =0 
    total_number_nucleotides = 0
    for line in fastq_file:
        count_lines +=  1
        number_sequence_id = count_lines/4
        number_characters += len(line)
        if count_lines%4 == 1: #modulus 
            total_number_nucleotides += len(line)
    average_length_lines = number_characters/count_lines
    average_length_with_sequences = total_number_nucleotides/number_sequence_id
    print(f"The number of lines is {count_lines}, the number of sequence-IDs {number_sequence_id}, the number of characters {number_characters}, total numbers of nucleotides {total_number_nucleotides} and average length {average_length_lines} and average length containing nucleotides {average_length_with_sequences}")

# important for this task is 
# to set the variable to 0 if you want to cummulate count, i.e. count_lines = 0
# if you want to add up count or length, use +=

#Quality control of the FASTQ file is getting length of file and seeing if you can divide line count by 4.

# %4 is a handy tool to use for FASTQ files as these are composed of 4 different lines per sequence.
# if you just want to look at a sequence you iterate through a line of modulus, i.e. 
# if you have 4lines as in FASTQ file: 0%4 it is 0, 1%4 is 1. 2%4 is 2....
# so when you are interested in the second line you need to set modulus if count_lines%4 == 1: #modulus 


# alterantively. you can also just count the lines starting with @
