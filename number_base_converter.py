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
        self._value = value
        self._base = base
    
    def __str__(self):
        return f'{self._value} in base {self._base}'
    
    # Currently not working    
    # def __int__(self):
    #     return f'{self.to_decimal()}'
        
    # Function to convert from a base to decimal
    def to_decimal(self):
        # Initialise power and output for looping
        power = 0 # first power
        total = 0 # output sum
        
        # Loop through characters, convert to decimal, then sum together and output
        for char in self._value[::-1]: # work in reverse in increasing powers
            
            # Convert numbers greater than ten to numeric if the base allows it
            if (self._base > 10) & (char == "X"):
                char = 10
            if (self._base > 11) & (char == "E"):
                char = 11
                
            # Check if any characters > base
            if int(char) > self._base:
                print("char " + char + " is greater than base ", str(self._base))
                break
    
            # Calculate output in decimal and add to total
            total += int(char) * self._base ** power
            power += 1 # increase power for each element
   
        # Output the total sum
        return(total)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# Testing
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
test = number_base("24", 12)

print(test._value)
print(test._base)
print(test.to_decimal())
print(test._value)
print(test._base)

print(test)
#int(test)
#str(test)
#print(to_decimal("19", 12))

# Make a from_decimal() function to any base
    # Loop through powers (increasing) of new base to figure out how many digits we need (use int function)
    # Loop through powers (descending) to assign values to a list or string (use int function)
    # Append list or string and output
    
# Make a class with all base conversions using the two functions 
    # e.g. to_dozenal could have an input base (string object with this information???) and output as dozenal
