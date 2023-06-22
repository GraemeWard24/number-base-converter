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
        
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
        # Initial checks
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
        # Check if valid base
        if base < 2 or base > 12:
            print(f'Please input a base between 2 and 12. Selected {base}')
            return
            # sys.exit()
        self.base = base
        
        # Check if value is valid
        # Make list of valid digits depending on base
        # Need to convert integers to strings
        valid_digits_int = list(range(1, 10))
        valid_digits = [''] * len(valid_digits_int)
        for i in range(0, len(valid_digits_int)):
            valid_digits[i] = str(valid_digits_int[i])
        
        # Add X and E if the base is high enough
        if base > 10:
            valid_digits.append("X")
        if base > 11:
            valid_digits.append("E")
            
        # Check each digit to see if it is valid
        for i in value:
            if i not in valid_digits:
                print(f'Non verified digit is {i}')
                return
                # sys.exit()
        self.value = value
        

    
    def __str__(self):
        return f'{self.value} in base {self.base}'
    
    # Currently not working    
    # def __int__(self):
    #     return f'{self.to_decimal()}'
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
    # Function to convert from a base to decimal
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
    def convert_to_decimal(self):
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
                
            # Check if any characters > base (need to do the same for X and E?)
            if int(char) > self.base:
                print("char " + char + " is greater than base ", str(self.base))
                return
    
            # Calculate output in decimal and add to total
            total += int(char) * self.base ** power
            power += 1 # increase power for each element
   
        # Output the total sum
        return(total)
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
    # Function to convert to any base
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
    def show_in_base(self, base_to):
        val = self.convert_to_decimal() # firstly convert value to decimal
        
        # Determine number of digits needed for new base
        max_power = 1 # iterator for number of digits required (start at power 1 as power 0 can use power 1 to solve)
        flag = False # initialise flag as false to be made true when we find the maximum power
        while flag == False:
            if int(base_to ** max_power / val) == 0: # if the floor of base ^ i / val is 0 then we need more power
                max_power += 1
                continue
            else:
                flag = True # we have enough power so exit loop
        
        # Place in a list 'max_power' elements long
        powers = list(range(max_power)) # initialise list
        for i in powers:
            powers[i] = base_to ** powers[i] # get powers needed to make the number in the particular base
        powers = powers[::-1] # reverse order so we start with highest powers first
        
        # Use integer division and mods to loop through and extract the digits in 'base_to'
        digits = [0] * len(powers) # initialise output (same length as powers)
        num_left = val # initialise the number left to assign (start with the whole thing)
        for i in range(len(powers)):
            digits[i] = num_left // powers[i] # assign to digits[0]
            num_left = num_left % powers[i] # pass on to next iteration of the loop
            
        # Concatenate digits together for output
        output = ""
        for i in digits:
            # Replace decimal digit with number base symbol
            if base_to > 10:
                if i == 10:
                    i = "X"
                elif i == 11:
                    i = "E"
            
            # Append
            output += str(i)
        
        return(output)
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
    # Functions to display in all bases
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
    # Function to show in binary/base 2
    def show_in_binary(self):
        return(self.show_in_base(2))
    
    # Function to show in ternary/base 3
    def show_in_ternary(self):
        return(self.show_in_base(3))
    
    # Function to show in quarternary/base 4
    def show_in_quarternary(self):
        return(self.show_in_base(4))
    
    # Function to show in quinary/base 5
    def show_in_quinary(self):
        return(self.show_in_base(5))
    
    # Function to show in seximal/base 6
    def show_in_seximal(self):
        return(self.show_in_base(6))
    
    # Function to show in septimal/base 7
    def show_in_septimal(self):
        return(self.show_in_base(7))
    
    # Function to show in octal/base 8
    def show_in_octal(self):
        return(self.show_in_base(8))
    
    # Function to show in nonary/base 9
    def show_in_nonary(self):
        return(self.show_in_base(9))
    
    # Function to show in decimal/base 10
    def show_in_decimal(self):
        return(self.show_in_base(10)) # don't use convert_to_decimal as we want str output for consistency
    
    # Function to show in elevenary/base 11
    def show_in_elevenary(self):
        return(self.show_in_base(11))
    
    # Function to show in dozenal/base 12
    def show_in_dozenal(self):
        return(self.show_in_base(12))
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
    # Function to change base of number
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
    # NEED TO ADD IN INITIAL CHECKS
    def change_value(self, value_to):
        # Set value in current base, call class to get value in that base
        self.value = value_to
        # self.value = number_base(value_to, self.base).show_in_base(self.base)
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
    # Function to change base of number
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
    # NEED TO ADD IN INITIAL CHECKS
    def change_base(self, base_to):
        self.value = self.show_in_base(base_to)
        self.base = base_to
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
    # Functions to change to all bases
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
    # Function to show in binary/base 2
    def to_binary(self):
        return(self.change_base(2))
    
    # Function to show in ternary/base 3
    def to_ternary(self):
        return(self.change_base(3))
    
    # Function to show in quarternary/base 4
    def to_quarternary(self):
        return(self.change_base(4))
    
    # Function to show in quinary/base 5
    def to_quinary(self):
        return(self.change_base(5))
    
    # Function to show in seximal/base 6
    def to_seximal(self):
        return(self.change_base(6))
    
    # Function to show in septimal/base 7
    def to_septimal(self):
        return(self.change_base(7))
    
    # Function to show in octal/base 8
    def to_octal(self):
        return(self.change_base(8))
    
    # Function to show in nonary/base 9
    def to_nonary(self):
        return(self.change_base(9))
    
    # Function to show in decimal/base 10
    def to_decimal(self):
        return(self.change_base(10)) # don't use convert_to_decimal as we want str output for consistency
    
    # Function to show in elevenary/base 11
    def to_elevenary(self):
        return(self.change_base(11))
    
    # Function to show in dozenal/base 12
    def to_dozenal(self):
        return(self.change_base(12))
    
    # Create methods to perform operations to object using a different number_base object
    

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# Testing
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
test = number_base("24", 12)

print(test)
test.change_base(8)
print(test)
test.change_value("40")
print(test)
print(test.show_in_decimal())
test.to_elevenary()
print(test)

print(test.show_in_decimal())

test.to_binary()
print(test)
print(test.show_in_decimal())
