import sys
import os
import random
from com.lloyd.base.Actors import Player
from com.lloyd.base.Actors import Mob
'''
class player(object):
    
    def __init__(self, name):
        self.name = name
        self.maxHealth = 100
        self.health = 10
        self.maxMana = 100
        self.mana = self.maxMana
        self.attack = 10

    def checkHp(self, amount):
        if self.health >= amount:
            return True
        return False

    def restoreHp(self, amount):
        self.health += amount
        if self.health > self.maxHealth:
            self.health = self.maxHealth

'''

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
        exitGame()
    else:
        main()

def start():
    clearScreen()
    print("Innkeeper: What is your name Traveller?")
    name = input("-> ")
    global playerIG
    playerIG = Player(name)
    start1()
    
def start1():
    clearScreen()
    print("Innkeeper: %s huh?" % playerIG.name)
    print("Innkeeper: I'm sure I've heard that name before.")
    leaveConvo = False
    while not leaveConvo:
        print("[1] Reply: I don't really know what to do next, can you help me? (Tutorial)")
        print("[2] Reply: Any news?")
        print("[3] Reply: Shut up and point me in the direction of the nearest foe that needs slaying.")
        print("[4] Leave Conversation")
        start1option = getIntInput()
        clearScreen()
        if start1option == 1:
            print("Hey this is the tutorial bit etc etc")
        if start1option == 2:
            print("Well shit's not too good here")
        if start1option == 3:
            print("Oh... okay.  Fight this!")
            startBattle()
        if start1option == 4:
            leaveConvo = True
        
    start2()

def start2():
    print("You are standing inside a bustling pub.  The innkeeper is eyeing you, and you don't know \nif it's true that he knows you or is simply weary of your presence.")
    leaveConvo = False
    while not leaveConvo:
        clearScreen()
        print("Would you like a drink, %s?" % playerIG.name)
        print("[1] Reply: Yes")
        print("[2] Reply: No")
        start2option = getIntInput()
        clearScreen()
        if start2option == 1:
            print("Have this.  It will make you feel better.")
            playerIG.adjustHp(50)
            print("%s HP is now %s / %s!" % (playerIG.name, playerIG.health, playerIG.maxHealth))
            if playerIG.checkHp(playerIG.maxHealth):
                leaveConvo = True
        elif start2option == 2:
            print("Are you sure?  You look a bit weak.")
    
    start1()

def startBattle():
    mob = randomMob()
    print("A wild %s approaches!" % mob.name)
    combat = True
    while combat:
        showVitals(mob)
        battleOption()
        option = getIntInput()
        if option == 1:
            playerIG.attackTarget(mob)
        
        if mob.health != 0:
            mob.aiScript(playerIG)
        
        if playerIG.health == 0:
            print("You lose!")
            exitGame()
        elif mob.health == 0:
            victory(mob)
            combat = False
            
def randomMob():
    rng = random.randint(1,1000)        
    if rng < 200:
        return Mob("Imp", 25, 30, 6, 0, 6) 
    elif rng < 500:
        return Mob("Goblin", 40, 10, 8, 2, 10)
    elif rng < 700:
        return Mob("Bite Bug", 20, 20, 6, 2, 4)
    else:
        return Mob("Cockblocker", 60, 50, 12, 4, 500)
    
def victory(mob):
    print("You have defeated %s!" % mob.name)
    print("You gain %i gold!" % mob.gold)
    playerIG.adjustGold(mob.gold) 
      
def battleOption():
    print("%s\'s turn" % playerIG.name)
    print("[1] Attack")

def showVitals(mob):
    print("%s HP: %i / % i  MP:  %i / %i" % (playerIG.name, playerIG.health, playerIG.maxHealth, playerIG.mana, playerIG.maxMana))
    print("%s HP: %i / % i  MP:  %i / %i" % (mob.name, mob.health, mob.maxHealth, mob.mana, mob.maxMana))

def getIntInput():
    return int(input("-> "))

def clearScreen():
    os.system("cls")
    
def exitGame():
    sys.exit()

main()