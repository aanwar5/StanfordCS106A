"""
File: liftoff.py
----------------------
This program writes out the calls for a spaceship that is about to launch.
It counts down the numbers from 10 to 1 and then writes “Liftoff!”
"""
import time

def main():
    for i in reversed(range(1,11)):
        time.sleep(1)
        print(i)
    if i == 1:
        print('Liftoff!')
        #if print(i) == 10:
       # print('liftoff!')


    pass


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()