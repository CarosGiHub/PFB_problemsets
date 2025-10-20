#!/usr/bin/env python3

# name = "caroline"
# print("my name is" , name)

# colour = "blue"
# print ("my favorite colour is" , colour)

# acitvity = "coding"
# print ('my favorite activity is' , acitvity)

# animal = "turtle"
# print ("my favorite animals are" , animal)

# #Try out f"" string formatting.

#print(f"My name: {name} and I love the colour {colour} that contrasts the colour of my favorite animal {animal} really well") 

#Try sys.argv
import sys

name = sys.argv[1]
colour = sys.argv[2]
animal = sys.argv[3]

print (name, " s favorite colour is" , colour, "and her favorite animals are" , animal)

