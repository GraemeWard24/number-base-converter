# Number Bases
We live in a Base Ten world, likely due to the fact we have ten fingers.
This means we have ten distinct digits for our mathematics.
It was a purely random and arbitrary choice.
What would life be like if we lived in a different world with a different number base?
Well, you can gain a taste of that life so stick around and read on!

## Instructions
The `number_base_converter.py` file contains:
* A `number_base` object, which takes a positive or negative integer or string `value` in the desired base and an integer `base` from 2-12 (which is in Base Ten).
* Inside this object you can both display the value in a different base with the `show_in_base()` method, or directly show in a base with the `show_in_...` where the base name is specified, e.g. `show_in_dozenal()`. See below for base names.
* You can also update the base with the `change_base()` method, which changes the base of the object. Again you could use the numeric `change_base(2)` method or use `change_to_binary()`.
* Operator function `add` which adds `number_base` objects together and outputs them as a `number_base` object in a desired base

Note that the digits for ten (known as dec) and eleven (known as el) are X and E respectively and are shown as such in higher bases.
There are no packages used so it's an easy plug and play script for fun times.

## Base names
* 2 - binary
* 3 - ternary
* 4 - quarternary
* 5 - quinary
* 6 - seximal
* 7 - septimal
* 8 - octal
* 9 - nonary
* 10/X - decimal
* 11/E - elevenary
* 12 - dozenal

## Future enhancements
* The values can only be integers. I am planning to add floating point numbers in so we can divide.
* Only addition exists so far. I will add subtraction, multiplication, exponentiation, and once floating points exist, division.
* I would like to use names of bases rather than numbers (as they are in base ten).
* I will eventually add more bases, possibly up to 16, or higher if I can devise a good naming technique for higher bases. I am not a fan of the A, B, C... system but might need to resort to that eventually.
