"""
File: hailstones.py
-------------------
This is a file for the optional Hailstones problem, if
you'd like to try solving it.
"""
import random

def main():

    total = 0
    while total <= 0:
     n_1 = random.randint(10, 99)
     n_2 = random.randint(10, 99)
     sol1 = str(n_1 + n_2)

     print(format("What is the solution " + str(n_1) + "+" + str(n_2) + " ? "))
     x = input(str("Insert Answer here "))
     if x == sol1:
       print("You selected the correct answer which is " + (x))
       print("Good Job!")
       total =  total + 1
       print("You got a total of " + str(total) + " correct")
     else:
        print("you selected the wrong answer")
        print("Expected answer is " + (sol1))
        print("You got a total of " + str(total) + " correct")
        total == 0
        print("You're back to square one with none correct")
        print("Get three correct in a row to win Chris and Mehrans love")


     while total <= 1:
         n_1 = random.randint(10, 99)
         n_2 = random.randint(10, 99)
         sol1 = str(n_1 + n_2)

         print(format("What is the solution " + str(n_1) + "+" + str(n_2) + " ? "))
         x = input(str("Insert Answer here "))
         if x == sol1:
             print("You selected the correct answer which is " + (x))
             print("Good Job!")
             total = total + 1
             print("You got a total of " + str(total) + " correct")
         else:
             print("you selected the wrong answer")
             print("Expected answer is " + (sol1))
             print("You got a total of " + str(total) + " correct")
             total = 0
             print("You're back to square one with none correct")
             print("Get three correct in a row to win Chris and Mehrans love")
     while total <= 2:
         n_1 = random.randint(10, 99)
         n_2 = random.randint(10, 99)
         sol1 = str(n_1 + n_2)

         print(format("What is the solution " + str(n_1) + "+" + str(n_2) + " ? "))
         x = input(str("Insert Answer here "))
         if x == sol1:
             print("You selected the correct answer which is " + (x))
             print("Good Job!")
             total = total + 1
             print("You got a total of " + str(total) + " correct")
         else:
             print("you selected the wrong answer")
             print("Expected answer is " + (sol1))
             print("You got a total of " + str(total) + " correct")
             total = 0
             print("You're back to square one with none correct")
             print("Get three correct in a row to win Chris and Mehrans love")
     if total ==3:
         print("Congratulations, you did it!")
         print("Mehran and Chris Luv u")













# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
