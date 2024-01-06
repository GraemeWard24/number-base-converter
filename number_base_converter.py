# -*- coding: utf-8 -*-
"""
Created on Tue May 9 2023

@author: Graeme
"""
#import os
#import sys
#import numpy as np
#import pandas as pd
import re

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# Define the number base class
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# value is a string (in case base is >10 with non-numeric symbols) of the value of the number in its native base
# base is the decimal representation of the native base
class number_base:
    '''Create a number base object with a value and a base'''

    # Set value of number and base of number in input
    def __init__(self, value, base):
        '''Set value (string or integer) and base (integer) to set up the number base object
        Perform checks of inputs (types and values) before allowing the user to continue'''

        # Perform checks on inputs
        # Check if valid base (integer between 2 and 12)
        self.__check_base(base) # outputs errors if invalid syntax

        # Set base - need it for value check
        self._base = base

        # Check if valid value (and output as it converts integer to string)
        value = self.__check_value(value) # outputs errors if invalid syntax

        # Set value
        self._value = value

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
    # Input check functions
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
    def __check_base(self, input_base):
        '''Check if valid base (integer between 2 and 12)'''

        # Needs to be integer
        if not isinstance(input_base, int):
            raise TypeError(f'Base should be integer, not {type(input_base)}')

        # Only allow bases between 2 and 12
        if input_base < 2 or input_base > 12:
            raise ValueError(f'Please input a base between 2 and 12. Selected {input_base}.')

    def __check_value(self, input_value):
        '''Check if valid value (integer or string with valid characters depending on base)'''

        # Allow for integer input, convert to string
        if isinstance(input_value, int) or isinstance(input_value, float):
            input_value = str(input_value)

        # Check if valid value (string with valid digits depending on selected base)
        if not isinstance(input_value, str):
            raise TypeError(f'Value should be integer, float, or string, not {type(input_value)}')
            
        # We can have zero or one floating point. If there is one then flag it as a floating point number
        num_fl_points = len(re.findall('\.', input_value)) # count of floating points
        if num_fl_points == 0:
            is_float = False
        elif num_fl_points == 1:
            is_float = True
        else:
            raise ValueError(f'Only 0 or 1 floating (decimal) place allowed. "{input_value}" has {num_fl_points}')

        # Check if value is valid, allowable characters depend on base.
        # '-' allowed at the front only, one '.' is allowed (taken care of above)
        # Make list of valid digits depending on base
        # Valid digits are 0 to (base - 1), or 9. 10, 11 taken care of
        valid_digits = list(range(min(self.base, 10)))
        valid_digits = [str(i) for i in valid_digits] # convert to strings

        # Add X and E if the base is high enough
        if self.base > 10:
            valid_digits.append('X')
        if self.base > 11:
            valid_digits.append('E')
            
        # We are allowed to have floating points, if more than one the code will not reach this point
        valid_digits.append('.')

        # Check each digit to see if it is valid - first digit can be '-' for negatives
        is_valid = [i in valid_digits for i in input_value] # get boolean for allowable elements

        # First element can be '-' for negatives
        if input_value[0] == '-':
            is_valid[0] = True
            is_negative = True # use in floating fixes for '-.1'
        else:
            is_negative = False

        # If any element of is_valid is False then we have bad characters
        # Show them and produce error
        if not all(is_valid):
            non_valid = [] # initialise non-valid list to output
            for i in range(len(input_value)): # loop through characters of value
                if not is_valid[i]:
                    non_valid.append(input_value[i])
            raise ValueError(f"Non verified digits identified. They are {non_valid} from input '{input_value}'")
            
        # Fix up floating format, '.xyz' -> '0.xyz', 'x.' -> 'x', 'x.000...' -> 'x'
        if is_float:
            # Add leading zero if none
            if not is_negative and input_value[0] == ".":
                input_value = "0" + input_value
            elif is_negative and input_value[1] == ".":
                input_value = "-0" + input_value[1:]
                
            # Remove trailing zeroes (or floating points as we will convert to integer when we can)
            # After we remove the floating point as the final digit, stop so we dont convert 10.0 to 1
            while (input_value[-1] == "0" and len(re.findall('\.', input_value)) == 1) or input_value[-1] == ".":
                input_value = input_value[:-1]
            
        return input_value # output the new value (number converted to string)
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
    # Symbol converter function
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
    def __convert_symbol_to_decimal(self, char, base):
        '''Sometimes we'll need to convert symbols to decimal representations for calculations
        This function does that so we can just call it when need be'''
        # Check character and base, if allowable, then convert to decimal representation,
        # else, convert to integer and output
        if char == "X" and base > 10:
            return 10
        elif char == "E" and base > 11:
            return 11
        else:
            return int(char)
        
    def __convert_symbol_from_decimal(self, char, base):
        '''Sometimes we'll need to convert symbols from decimal representations for calculations
        This function does that so we can just call it when need be'''
        # Check character and base, if allowable, then convert to decimal representation,
        # else, convert to integer and output
        if char == 10 and base > 10:
            return "X"
        elif char == 11 and base > 11:
            return "E"
        else:
            return str(char)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
    # Restrict access to changing value and base using nb.value or nb.base = foo
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
    # Use property decorator and setter decorator to reference and error user updates
    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, value):
        raise AttributeError('Use change_base() method to change base')

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        raise AttributeError('Use change_value() method to change value')

    # String output is information about the value and the base
    def __str__(self):
        return f'{self.value} in base {self.base}'

    # Integer output is the value converted to decimal coerced to integer
    def __int__(self):
        return int(self.__convert_to_decimal())

    # Float output is the value converted to decimal coerced to float
    def __float__(self):
        return float(self.__convert_to_decimal())

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
    # Function to convert from a base to decimal
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
    def __convert_to_decimal(self):
        '''Convert the value to decimal, crucial for changing bases'''
        # Initialise output for looping
        total = 0 # output sum
        
        # Add flag for if negative number

        value = self.value[:] # get value but a different instance as we don't want to overwrite
        if value[0] == "-":
            value = value[1::] # remove the negative, add it back on at the end
            negative_flag = True
        else:
            negative_flag = False
            
        # Determine if a floating point
        is_float = len(re.findall('\.', value)) # 0 for integer, 1 for float
        
        # If floating point, split into the two bits, otherwise the whole thing is an integer
        if is_float:
            integer_part = value.split('.')[0]
            float_part = value.split('.')[1]
        else:
            integer_part = value[:]
            
        # Convert integer part to decimal
        # Final digit is base ** 0, then next in reverse order is base ** 1 and so on
        power = 0 # first power
        # Loop through characters, convert to decimal, then sum together and output
        for char in integer_part[::-1]: # work in reverse in increasing powers
            
            # Convert numbers greater than ten to numeric if the base allows it, otherwise just make int
            char = self.__convert_symbol_to_decimal(char, self.base)

            # Calculate output in decimal and add to total
            total += char * self.base ** power
            power += 1 # increase power for each element
        
        # Convert floating part to decimal if it exists
        # First digit is base ** -1, then next is base ** -2 and so on)
        if is_float:
            power = -1 # first power
            # Loop through characters, convert to decimal, then sum together and output
            for char in float_part: # work in forward order in decreasing powers
            
                # Convert numbers greater than ten to numeric if the base allows it, otherwise just make int
                char = self.__convert_symbol_to_decimal(char, self.base)
         
                # Calculate output in decimal and add to total
                total += char * self.base ** power
                power -= 1 # decrease power for each element

        # Output the total sum
        if negative_flag:
            return total * -1
        else:
            return total

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
    # Function to convert to any base
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
    def show_in_base(self, base_to):
        '''Allow the user to see the number in any base, does not change the number base object'''

        # Check if valid base (integer between 2 and 12)
        self.__check_base(base_to) # outputs errors if invalid syntax

        val = self.__convert_to_decimal() # firstly convert value to decimal
        
        # If value is 0, return as 0 (don't want to divide by zero later)
        if val == 0:
            return str(val)
        
        # Check if negative, if so, remove negative and flag as negative to add back on
        if val < 0:
            val = abs(val)
            negative_flag = True
        else:
            negative_flag = False
            
        # Split into integer and float parts
        # For integer we do num / base. Mod part is 0's value (convert symbols), integer part moves on
        # Then do new_num (the integer bit) / base. Mod part is 10's value, integer part moves on
        int_val = int(val)
        
        # If integer part is 0 to start, set output as 0 and move on
        if int_val == 0:
            int_part = "0"
        else:
            digits_rev = list() # initialise output list (will build in reverse)
            while int_val > 0:
                # Extract mod first before we update int_val
                new_digit = divmod(int_val, base_to)[1]
                new_digit = self.__convert_symbol_from_decimal(new_digit, base_to) # Update digit to X or E
                digits_rev.append(new_digit) # mod part
                int_val = divmod(int_val, base_to)[0] # int part
                
            # Now reverse digits to get int_part as we built up from ones to '10s' and so on
            # Then convert to strings and concatenate to get the integer digit
            int_part = ''.join([str(i) for i in digits_rev[::-1]])

        # For float part, we do num * base (technically divide by base ** -1),
        # Integer part is 0.1's value, mod moves on
        # Then we do new_num (the mod bit) * base. Integer part is 0.01's value, mod part moves on
        fl_val = val - int(val)
        if fl_val != 0:
            digits = list() # initialise output list
            while len(digits) <= 16:
                # Append digit first before we update fl_val
                new_digit = int(fl_val * base_to) # add in '10 ** -x' bit
                new_digit = self.__convert_symbol_from_decimal(new_digit, base_to) # Update digit to X or E
                digits.append(new_digit) # add in '10 ** -x' bit
                fl_val = (fl_val * base_to) - int(fl_val * base_to) # new fl_val to calculate next digit
                
            # Convert to strings and concatenate to get the floating digit, add a floating point at the start
            fl_part = '.' + ''.join([str(i) for i in digits])
        else:
            fl_part = ''
            
        # Concatenate integer and floating parts to get the output
        output = int_part + fl_part
        
        # Output based on if negative or positive
        if negative_flag:
            return "-" + output
        else:
            return output


    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
    # Functions to display in all bases using base names, not numbers
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
    # Function to show in binary/base 2
    def show_in_binary(self):
        return self.show_in_base(2)

    # Function to show in ternary/base 3
    def show_in_ternary(self):
        return self.show_in_base(3)

    # Function to show in quarternary/base 4
    def show_in_quarternary(self):
        return self.show_in_base(4)

    # Function to show in quinary/base 5
    def show_in_quinary(self):
        return self.show_in_base(5)

    # Function to show in seximal/base 6
    def show_in_seximal(self):
        return self.show_in_base(6)

    # Function to show in septimal/base 7
    def show_in_septimal(self):
        return self.show_in_base(7)

    # Function to show in octal/base 8
    def show_in_octal(self):
        return self.show_in_base(8)

    # Function to show in nonary/base 9
    def show_in_nonary(self):
        return self.show_in_base(9)

    # Function to show in decimal/base 10
    def show_in_decimal(self):
        return self.show_in_base(10) # don't use __convert_to_decimal as we want str output for consistency

    # Function to show in elevenary/base 11
    def show_in_elevenary(self):
        return self.show_in_base(11)

    # Function to show in dozenal/base 12
    def show_in_dozenal(self):
        return self.show_in_base(12)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
    # Function to change value of number base object
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
    def change_value(self, value_to):
        '''Allow the user to change the value of the number base object'''

        # Check if valid value (and output as it converts integer to string)
        value_to = self.__check_value(value_to) # outputs errors if invalid syntax

        # Just update value once checks are complete
        self._value = value_to

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
    # Function to change base of number base object
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
    def change_base(self, base_to):
        '''Allow the user to change the base of the number base object'''

        # Check if valid base (integer between 2 and 12)
        self.__check_base(base_to) # outputs errors if invalid syntax

        # Update the value to the new base and then update the base
        self._value = self.show_in_base(base_to)
        self._base = base_to

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
    # Functions to change to all bases
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
    # Function to show in binary/base 2
    def to_binary(self):
        return self.change_base(2)

    # Function to show in ternary/base 3
    def to_ternary(self):
        return self.change_base(3)

    # Function to show in quarternary/base 4
    def to_quarternary(self):
        return self.change_base(4)

    # Function to show in quinary/base 5
    def to_quinary(self):
        return self.change_base(5)

    # Function to show in seximal/base 6
    def to_seximal(self):
        return self.change_base(6)

    # Function to show in septimal/base 7
    def to_septimal(self):
        return self.change_base(7)

    # Function to show in octal/base 8
    def to_octal(self):
        return self.change_base(8)

    # Function to show in nonary/base 9
    def to_nonary(self):
        return self.change_base(9)

    # Function to show in decimal/base 10
    def to_decimal(self):
        return self.change_base(10) # don't use __convert_to_decimal as we want str output for consistency

    # Function to show in elevenary/base 11
    def to_elevenary(self):
        return self.change_base(11)

    # Function to show in dozenal/base 12
    def to_dozenal(self):
        return self.change_base(12)
  
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# Testing
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
test = number_base('-1E2', 12)
test2 = number_base('24', 9)
test3 = number_base(0, 5)
test4 = number_base("12.1", 5)
test5 = number_base("-.1", 5)
test6 = number_base("1.3333333", 10)
test7 = number_base("10.000", 6)
test3.show_in_binary()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# Operation functions - don't include in class but make the inputs number base objects
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# This means we can do this like add(nb1, nb2, nb3) rather than nb1.add(nb2), nb1.add(nb3)
def add(*args, base = 10):
    '''Add number base objects together and output in a specified base'''
       
    # Get total value of args by summing
    total = 0 # initialise
    for nb in args:
        # Check if the input is a number base object
        if not isinstance(nb, number_base):
            raise TypeError(f'Inputs must be number_base objects, not {type(nb)}')
        
        # Add all elements
        total += float(nb) # int is value of nb object in decimal
    
    # Now convert total to a number base object with output base
    out = number_base(total, 10) # total is count in decimal
    out.change_base(base) # Change base to the output base
    return out

def multiply(*args, base = 10):
    '''Multiply number base objects together and output in a specified base'''
       
    # Get total value of args by summing
    total = 1 # initialise
    for nb in args:
        # Check if the input is a number base object
        if not isinstance(nb, number_base):
            raise TypeError(f'Inputs must be number_base objects, not {type(nb)}')
        
        # Add all elements
        total *= float(nb) # int is value of nb object in decimal
    
    # Now convert total to a number base object with output base
    out = number_base(total, 10) # total is count in decimal
    out.change_base(base) # Change base to the output base
    return out

add_test = add(test, test, number_base(100, 7), base = 12)
str(add_test)
add_test.value

# Output will be number base object with user defined base (include a default)
# Use *args so user can have as many objects in calculation

# Add number bases together
#def add(*args):
#    # Convert both to decimal and add together. Place this in a decimal number base then output in self.base
#    output = number_base(str(self.__convert_to_decimal() + num_base.__convert_to_decimal()), 10)
#    return(output.show_in_base(self.base)) # currently outputting new value but could add to first object

# Subtract a number in any base to the current object
#def subtract(self, num_base):
#    # Convert both to decimal and add together. Place this in a decimal number base then output in self.base
#    output = number_base(str(self.__convert_to_decimal() - num_base.__convert_to_decimal()), 10)
#    return(output.show_in_base(self.base))
  
# Multiply a number in any base to the current object
#def multiply(self, num_base):
#    # Convert both to decimal and add together. Place this in a decimal number base then output in self.base
#    output = number_base(str(self.__convert_to_decimal() * num_base.__convert_to_decimal()), 10)
#    return(output.show_in_base(self.base))

# Divide a number in any base to the current object
#def divide(self, num_base):
#    # Convert both to decimal and add together. Place this in a decimal number base then output in self.base
#    output = number_base(str(self.__convert_to_decimal() / num_base.__convert_to_decimal()), 10)
#    return(output.show_in_base(self.base))
