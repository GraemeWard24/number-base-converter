# -*- coding: utf-8 -*-
"""
Created on Tue May 9 2023

@author: Graeme
"""
#import os
#import sys
#import numpy as np
#import pandas as pd

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# Define the number base class
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# value is a string (in case base is >10 with non-numeric symbols) of the value of the number in its native base 
# base is the decimal representation of the native base
class number_base:
    # Set value of number and base of number in input
    def __init__(self, value, base):
        self.value = value
        self.base = base
    
    def __str__(self):
        return f'{self.value} in base {self.base}'
    
    # Currently not working    
    # def __int__(self):
    #     return f'{self.to_decimal()}'
        
    # Function to convert from a base to decimal
    def to_decimal(self):
        # Initialise power and output for looping
        power = 0 # first power
        total = 0 # output sum
        
        # Loop through characters, convert to decimal, then sum together and output
        for char in self.value[::-1]: # work in reverse in increasing powers
            
            # Convert numbers greater than ten to numeric if the base allows it
            if (self.base > 10) & (char == "X"):
                char = 10
            if (self.base > 11) & (char == "E"):
                char = 11
                
            # Check if any characters > base
            if int(char) > self.base:
                print("char " + char + " is greater than base ", str(self.base))
                break
    
            # Calculate output in decimal and add to total
            total += int(char) * self.base ** power
            power += 1 # increase power for each element
   
        # Output the total sum
        return(total)
    
    # Function to convert from decimal to any base
    def from_decimal(self, base_to):
        val = self.to_decimal() # firstly convert value to decimal
        
        # Determine number of digits needed for new base
        i = 1 # iterator for number of digits required (start at power 1 as power 0 can use power 1 to solve)
        flag = False # initialise flag as false to be made true when we find the maximum power
        while flag == False:
            if int(base_to ** i / val) == 0: # if the floor of base ^ i / val is 0 then we need more power
                i += 1
                continue
            else:
                flag = True # we have enough power so exit loop
        
        # Now we need to find the values, place in a list 'i' elements long
        #digits = [0] * i # initialise list
        #for j in digits:
        #    digits[j] # get powers needed to make the number in the particular base
        
        
        return(val)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# Testing
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
test = number_base("24", 12)

print(test.from_decimal(9))

#print(test.value)
#print(test.base)
#print(test.to_decimal())

#print(test)

# Make a from_decimal() function to any base
    # Loop through powers (increasing) of new base to figure out how many digits we need (use int function)
    # Loop through powers (descending) to assign values to a list or string (use int function)
    # Append list or string and output
    
# Make a class with all base conversions using the two functions 
    # e.g. to_dozenal could have an input base (string object with this information???) and output as dozenal
