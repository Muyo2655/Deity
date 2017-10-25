'''
Created on Oct 25, 2017

@author: lloyd
'''
import sys
import os
import random
# roll a random 1 to 10000 integer
def randomInt():
    return random.randint(1,10000)
# will take a value and make it negative
def negate(value):
    value = int(value)
    return value - (value * 2)
# capture integer input from the user
def getIntInput():
    return int(input("-> "))
# clear the console screen of output
def clearScreen():
    os.system("cls")
# exit the game completely    
def exitGame():
    sys.exit()