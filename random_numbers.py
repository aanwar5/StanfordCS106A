"""
File: random_numbers.py
-----------------------
This program prints a series of random numbers in the
range from MIN_RANDOM to MAX_RANDOM, inclusive
"""

import random

def main():
     randomlist = random.sample(range(0, 100), 10)
     print(randomlist)
     nums = randomlist
     max(randomlist)
     print("Your maxiumum number is " + str(max(randomlist)))
     min(randomlist)
     print("Your minimumum number is " + str(min(randomlist)))




# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
