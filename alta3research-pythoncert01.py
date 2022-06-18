#!/usr/bin/env python3
"""Game that that uses the crayons library"""

#install the crayons package
#python3 -m pip install crayons
#import crayons package. Statement always goes on top before main code
import crayons

#print welcome to my python game title in bold red. Let the user know they have 10 tries to guess the number
print(crayons.red(f"Hello, Welcome to my Python game.\nCan you guess the number I'm thinking?. You have 10 tries", bold=True))

"""run time code. Always indent under function"""
def status():
    #set count to 10
    count = 10

    while count > 0:
        #ask user to input any number
        user_input = int(input("Enter the number: "))
        #if input is correct number
        if user_input == 23:
            #display 'YOU WIN' in bold green
            print(crayons.green(f"YOU WIN", bold=True))
            print(crayons.yellow(f"The game has ended. Goodbye!", bold=True))
            break
        #if incorrect number, display 'Wrong answer...' message. The count will decrease by 1
        print(crayons.blue(f"Wrong answer. You have {count-1} attempts remaining....", bold=True))
        count = count - 1 
    else:
        #when counter reaches 0, user lost game
        print(crayons.yellow(f"Sorry you lost the game :(", bold=True))

def main():
    status()
main()
