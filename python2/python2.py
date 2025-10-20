#!/usr/bin/env python3
#always add the line above so that the script can run smoothly.

# slogan = "XXXXXXXPIRATESXXXX"

# if "PIRATES" in slogan:
#     print("aye captain")
# else:
#     print("not true")  

# Task 2 if/else 

# number = 1
# if number >=0:
#     print("positive")
# else:
#     print("negative")

# Task3 nested tests

# number = 1

# if number == 0:
#     print("0")
# elif number > 0:
#     print("positive")
#     if number < 50:
#         print("it is an even number that is smaller than 50")
# else:
#     print("negative")

# Task4 - if its an even number, the remainder if it is divided by 2 is 0 - that is reflected by the % sign

# number = 10
# if number == 0:
#     print("0")
#     if number % 2 == 0:
#             print("it is an even number")
# elif number > 0:
#     print("positive")
#     if number < 50:
#         print("it is a number that is smaller than 50")
#         if number % 2 == 0:
#             print("it is an even number that is smaller than 50")
# else:
#     print("negative")

# #Task 5 add additional if...

# number = -60
# if number == 0:
#     print("0")
#     if number % 2 == 0:
#             print("it is an even number")
# elif number > 0:
#     print("positive")
#     if number < 50:
#         print("it is a number that is smaller than 50")
#         if number % 2 == 0:
#             print("it is an even number that is smaller than 50")
#     if number > 50:
#             if number % 3 == 0:
#                 print("it is a number that is divisible by three")
#             if number % 2 == 0:
#                 print("it is an even number that is smaller than 50")     
# else:
#     print("negative")
#     if number % 2 == 0:
#             print("it is an even number that is smaller than 50")
#     if number % 3 == 0:
#         print("it is a number that is divisible by three")

#Sys Task
#important message here: sys.argv[] has string as input. One needs to convert it into integer to make it work
#let it run a number in the command line 
#int()

import sys

number = int(sys.argv[1])

if number == 0:
    print("0")
    if number % 2 == 0:
        print("it is an even number")
elif number > 0:
    print("positive")
    if number < 50:
        print("it is a number that is smaller than 50")
        if number % 2 == 0:
            print("it is an even number that is smaller than 50")
    if number > 50:
            if number % 3 == 0:
                print("it is a number that is divisible by three")
            if number % 2 == 0:
                print("it is an even number that is smaller than 50")     
else:
    print("negative")
    if number % 2 == 0:
            print("it is an even number that is smaller than 50")
    if number % 3 == 0:
        print("it is a number that is divisible by three")


#if you want to create a script - use the Visual Studio Code - Create New Phyton - Save File (name file here)
#make sure it is in the right folder/directory

#if a new directory is needed - mkdir command

#always be sure that you work in the right directory 
#otherwise use cd nameofthedirectory
#cd PFB_problemsets
#you can write a few letter of the direction and use the tab function to make it complete the fields

# if I want to carry out the script - I write the following in the terminal 
#python3 python2(name of the script) 
#press enter

#if you need to push document from local repository to digital one you need to run git push
#for this 
#a) run in the command line:
#git status (gives you information about the status - is there a document that is not synced yet - depicted in red)
#git add python2.py(the document you would like to add)
#git commit -m "writewhatthecommitdoes" (no parethesis needed around "writewhatthecommitdoes")
#if it shows the following that is fine you can ignore it: "hint: The '.git/hooks/pre-commit' hook was ignored because it's not set as executable.
#hint: You can disable this warning with `git config set advice.ignoredHook false`"
#git push
#type in assigned password key
#synch GitHub online and check if the document was synced
#git status (check if there is not document left that is unassigned. every unassigned document is shown in red)

#Important short cuts
# command + S: save
# command + /: makes text in #green
#tab - adds directories or assigned variables
#arrow up - helps to find previous commands

