# -*- coding: utf-8 -*-
"""
Created on Tue May 9 2023

@author: Graeme
"""
# Function to convert from a base to decimal
def to_decimal(num_input, base):
   # Initialise power and output for looping
   power = 0 # first power
   total = 0 # output sum
   

   
   # Loop through characters, convert to decimal, then sum together and output
   for char in num_input[::-1]: # work in reverse in increasing powers
   
       # Convert numbers greater than ten to numeric if the base allows it
       if (base > 10) & (char == "X"):
           char = 10
       if (base > 11) & (char == "E"):
           char = 11
    
       # Check if any characters > base
       if int(char) > base:
           print("char " + char + " is greater than base ", str(base))
           break
    
       # Calculate output in decimal and add to total
       total += int(char) * base ** power
       power += 1 # increase power for each element
   
   # Output the total sum
   return(total)

print(to_decimal("19", 12))

# Make a from_decimal() function to any base
    # Loop through powers (increasing) of new base to figure out how many digits we need (use int function)
    # Loop through powers (descending) to assign values to a list or string (use int function)
    # Append list or string and output
    
# Make a class with all base conversions using the two functions 
    # e.g. to_dozenal could have an input base (string object with this information???) and output as dozenal
