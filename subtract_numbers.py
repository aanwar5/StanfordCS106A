"""
File: subtract_numbers.py
-------------------------
This program gets two real-values from the user and prints
the first number minus the second number.
"""


def main():
    #Prompts user for input
    num1 = input("Insert number here: ")
    num1 = float(num1)
    #prints users first input
    print("Your number is " + str(num1))
    #Prompts user for second input
    num2 = input("Insert Second Number here: ")
    num2 = float(num2)
   #prints user's second input
    print("Your second number is " + str(num2))
    #calculation-subtraction
    final = num1 - num2
    #prints final value
    print("The Final Subtraction is " + str(final))

    pass


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
