import random
import com.lloyd.base.Utils as util
import com.lloyd.base.Text as txt
from com.lloyd.base.Actors import Player
from com.lloyd.base.Actors import Mob

jobSelect = {
    1:"warrior",
    2:"cleric",
    3:"wizard"
}

def load():
    pass

def main():
    util.clearScreen()
    print("DEITY 0.1\n")
    for i in range(0, 3):
        print(txt.options[i] + txt.newMenu[i])
        
    option = util.getIntInput()
    
    if option == 1:
        start()
    elif option == 2:
        pass
    elif option == 3:
        util.exitGame()
    else:
        main()

def start():
    util.clearScreen()
    
    global playerIG
    name = chooseName()
    job = chooseJob()
    playerIG = Player(name, job, 50)
    start1()

# probably needs a regex validation to keep it alpha-limited
def chooseName():
    print(txt.newGame[4])
    return input("-> ")

# also needs validation so that they select 1 through 3
def chooseJob():
    print(txt.newGame[5])
    for i in range(6, 9):
        print(txt.options[i-6] + txt.newGame[i])
    return jobSelect[util.getIntInput()]
    
def start1():
    util.clearScreen()
    print("Innkeeper: %s huh?" % playerIG.name)
    print(txt.newGame[9])
    leaveConvo = False
    while not leaveConvo:
        convoSize = 4
        for x in range (0, convoSize):
            print(txt.options[x] + txt.newGame[x])
            
        start1option = util.getIntInput()
        util.clearScreen()
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
    print(txt.newGame[10])
    leaveConvo = False
    drinkCost = 5
    while not leaveConvo:
        util.clearScreen()
        print("Would you like a drink, %s?" % playerIG.name)
        print("It'll cost you " + str(drinkCost) + " gold.")
        txt.yesNo()
        start2option = util.getIntInput()
        util.clearScreen()
        if start2option == 1:
            buyDrink(drinkCost)
            if playerIG.checkHp(playerIG.maxHealth):
                leaveConvo = True
        elif start2option == 2:
            print(txt.newGame[11])
            leaveConvo = True
    
    start1()

def buyDrink(cost):
    canBuy = playerIG.checkGold(cost)
    
    if canBuy:
        print(txt.newGame[12])
        playerIG.adjustHp(50)
        playerIG.adjustGold(util.negate(5))
        print("%s HP is now %i / %i!" % (playerIG.name, playerIG.health, playerIG.maxHealth))
    else:
        print(txt.generic[2])

def startBattle():
    mob = randomMob()
    combat = True
    while combat:
        showVitals(mob)
        battleOption()
        option = util.getIntInput()
        if option == 1:
            playerIG.attackTarget(mob)
        elif option == 2:
            playerIG.scanTarget(mob)
        
        if mob.health != 0:
            mob.aiScript(playerIG)
            
        if playerIG.health == 0:
            loseBattle()
            combat = False
        elif mob.health == 0:
            victory(mob)
            combat = False
            
def randomMob():
    return Mob("Drunk Brawler", random.uniform(0.5, 0.8), random.randint(4,8))
 
def loseBattle():   
    print(txt.battle[2])
    playerIG.adjustGold(util.negate(playerIG.gold / 2))
    
def victory(mob):
    print("You have defeated %s!" % mob.name)
    print("You gain %i gold!" % mob.gold)
    playerIG.adjustGold(mob.gold) 
      
def battleOption():
    print("%s\'s turn" % playerIG.name)
    for i in range(0, 2):
        print(txt.options[i] + txt.battle[i])

def showVitals(mob):
    print("%s HP: %i / % i  MP:  %i / %i" % (playerIG.name, playerIG.health, playerIG.maxHealth, playerIG.mana, playerIG.maxMana))
    print("%s HP: %i / % i  MP:  %i / %i" % (mob.name, mob.health, mob.maxHealth, mob.mana, mob.maxMana))

main()