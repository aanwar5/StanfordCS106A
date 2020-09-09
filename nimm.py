"""
File: nimm.py
-------------------------
Add your comments here.
"""


def main():
   stones = 20
   #Player 1
   choice1 = 0
   #Player 1
   choice2 = 0
   print("There are", (stones), 'stones left')
   while (stones != 0 or stones >0 ):
       #Player 1 inputs
       choice1 = int(input("Player 1 would you like to remove 1 or 2 stones? "))
       while (choice1 != 1 and choice1 !=2) :
        choice1 = int(input('Please enter 1 or 2: '))
        #stones = stones
       stones = stones - choice1
       if stones > 0:
        print("You have", (stones), 'stones remaining')
       if stones < 1 :
           print("There are 0 stones left")
           print("Player 2 has won")
           break
       choice2 = int(input("Player 2 would you like to remove 1 or 2 stones ?"))
       while (choice2 != 1 and choice2 !=2) :
        choice2 = int(input('Please enter 1 or 2: '))
        #stones = stones
       stones = stones - choice2
       if stones > 0:
        print("You have", (stones), 'stones remaining')
       if stones < 1 :
           print("There are 0 stones")
           print("Player 1 has won")
           break

   pass


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
