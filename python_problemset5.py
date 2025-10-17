#!/usr/bin/env python3

# #Question1
fav_dict = {"book" : "ToTheLighthouse" , "song" : "LuckyYou" , "tree" : "Cedar"}
print(fav_dict)

# #Question2 use name of dict [] to access the value related to key book
print(fav_dict["book"])

# #Question3
#other way of doing question two - using a variable to key we are using
fav_thing = 'book'
print(fav_dict[fav_thing])

# #Question4:
print(fav_dict["tree"])

# #Question5:
#Add a new key/value pair to dictionary
fav_dict["organism"] = "Mice"
print(fav_dict)

# Make organism the new key of fav_thing
fav_thing = 'organism'
print(fav_dict[fav_thing])

#Question6
# to print out each key and value, in a for loop, one has to iterate the key in the dictinonary
for fav_things_key in fav_dict:
    fav_things_value = fav_dict[fav_things_key] #if you want to retrieve the information from the dict you shoul as access the associated value of the key by using this code
    print(fav_things_key , fav_things_value) #print key and variable

#Question7
# import sys

# # fav_dict = {"book" : "ToTheLighthouse" , "song" : "LuckyYou" , "tree" : "Cedar"}
# print("If you want to ")
# fav_thing = sys.argv[1]
# print(f"My favorite {fav_thing} is {fav_dict[fav_thing]}")
# to run this one has to put in the directory of the file and the key 
# (base) pfb@info07 PFB_problemsets % /usr/bin/python3 /Users/pfb/PFB_problemsets/python_problemset5.py organism
# sys.argv is counting the "items" in the command line: the file name is the first one in the command line => sys.argv[0]
# rhe typed in key is the second one => sys.argv[1]
# CAVE: you cannot run the Pfeil in the upper corner of the VisualCode for this, you have to use the command line to enter key and enter
# otherwise this does not work

# #Question8
# for fav_things_key in fav_dict:
#     print(fav_things_key)
# print("Choose your key")
# x = input()
# print('The key you chose is ' + x)

#Example for enter on website
# print('Enter your name:')
# x = input()
# print('Hello, ' + x)

# Alternative way to solve Question 8:
# print(fav_dict.keys()) - returns keys
# print(fav_dict.values()) - returns values
# print(fav_dict.items()) - returns tuple key/value pair

# Question 9:
#add new value to key - there is just one key per dictionary, 
# if the value gets changed it overwrites the old assignment
fav_dict["organism"] = "Human"
print(fav_dict)

#whatever gets printed in - change to other key
# import sys
# fav_thing = sys.argv[1]
# fav_dict[fav_thing] = sys.argv[2]
# print(f" My {fav_thing} is {fav_dict[fav_thing]}")

#this time use a third item in the command line that should replace the value

mySet = set('ATGTGGG')
mySet2 = {'ATGTGGG'}

print(mySet)
print(mySet2)
