'''
Created on Oct 22, 2017

@author: lloyd
'''

import random

class Actor(object):
    
    def __init__(self, name, health, mana, attack, defense, gold):
        self.name = name
        self.health = health
        self.maxHealth = 100
        self.mana = mana
        self.maxMana = 100
        self.attack = attack
        self.defense = defense
        self.gold = gold
     
    def checkHp(self, amount):
        if self.health >= amount:
            return True
        return False
       
    def adjustHp(self, amount):
        self.health += amount
        if self.health > self.maxHealth:
            self.health = self.maxHealth
        elif self.health < 0:
            self.death()
    
    def death(self):
        print("%s has perished!" % self.name)
        
    def printOutput(self, target, output):
        print("%s attacks %s for %i damage." % (self.name, target.name, output))
        
class Player(Actor):
    
    def __init__(self, name):
        Actor.__init__(self, name, 50, 50, 10, 4, 50) 
        
    def adjustGold(self, amount):
        self.gold += amount
           
    def checkGold(self, amount):
        if(self.gold >= amount):
            return True
        return False
    
    def attackTarget(self, target):
        rng = random.randint(1,1000)
        output = 0
        if rng < 100:
            output = target.defense - self.attack * 2
        else:
            output = target.defense - self.attack
        
        self.printOutput(target, abs(output))
        target.adjustHp(output)
        
        
class Mob(Actor):
    
    def __init__(self, name, health, mana, attack, defense, gold):
        Actor.__init__(self, name, health, mana, attack, defense, gold)
        self.maxHealth = self.health
        self.maxMana = self.mana
        
    def aiScript(self, target):
        rng = random.randint(1,1000)
        output = 0
        if rng < 250:
            output = target.defense - self.attack * 2
        else:
            output = target.defense - self.attack
            
        self.printOutput(target, abs(output))
        target.adjustHp(output)
        