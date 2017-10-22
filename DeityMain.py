import sys
import os
import random

class player:
    def __init__(self, name):
        self.name = name
        self.maxHealth = 100
        self.health = self.maxHealth
        self.maxMana = 100
        self.mana = self.maxMana
        self.attack = 10

def clearScreen():
    os.system("cls")

def load():
    pass

def main():
    clearScreen()
    print("DEITY 0.1\n")
    print("[1] Start")
    print("[2] Load")
    print("[3] Exit")
    option = int(input("-> "))
    if option == 1:
        start()
    elif option == 2:
        pass
    elif option == 3:
        sys.exit()
    else:
        main()

def start():
    clearScreen()
    print("Innkeeper: What is your name Traveller?")
    option = input("-> ")
    global playerIG
    playerIG = player(option)
    start1()

def start1():
    clearScreen()
    print("Innkeeper: %s huh?" % playerIG.name)
    print("Innkeeper: I'm sure I've heard that name before.")
    leaveConvo = False
    while not leaveConvo:
        print("[1] Reply: I don't really know what to do next, can you help me? (Tutorial)")
        print("[2] Reply: Any news?")
        print("[3] Reply: Shut up and point me in the direction of the nearest brothel.")
        print("[4] Leave Conversation")
        start1option = int(input("-> "))
        if start1option == 1:
            os.system("cls")
            print("Hey this is the tutorial bit etc etc")
        elif start1option == 2:
            os.system("cls")
            print("Well shit's not too good here")
        if start1option == 3:
            os.system("cls")
            print("Nearest brothel is over there")
        if start1option == 4:
            leaveConvo = True
    start2()

def start2():
    clearScreen()
    print("You are standing inside a bustling pub.  The innkeeper is eyeing you, and you don't know \nif it's true that he knows you or is simply weary of your presence.")
    start2option = int(input("-> "))


main()

