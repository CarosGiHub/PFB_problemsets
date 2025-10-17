#!/usr/bin/env python3

# #I saved the .txt file in the problemset folder. Next, I need to open and read it
# silverman_songtext = open("Python_07_nobody.txt", "r")

# # for line in silverman_songtext:
#     # print(line)

# songtext_string = silverman_songtext.read()

# #Question1:
# #search for "nobody" in songtext with re
# import re
# search_result = re.search("Nobody", songtext_string)
# print(search_result)

# #songtext = string for the file openend

# for found in re.finditer(r"(Nobody)" , songtext_string):
#     print(found)
#     # print(found.start())
#     # print(found.end())

# #Question 2:
# new_songtext = re.sub(r"Nobody" , r"Somebody" , songtext_string)
# print(new_songtext)

# #next I have to write an output 
# with open("Python_07_nobody.txt", "r") as silverman_songtext_read, open("Python_07_somebody.txt", "w") as silverman_songtext_read:
#     silverman_songtext_read.write(new_songtext)

#Question3:
import re

with open("Python_07fasta.txt", "r") as seq_file:
    fasta_file_string = seq_file.read()

for starter_found in re.finditer(r"(^>\w+)" , fasta_file_string, re.M):
    print(starter_found)
  
