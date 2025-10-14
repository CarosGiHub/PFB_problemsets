#!/usr/bin/env python3

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

# #Task 5 
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