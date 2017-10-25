'''
Created on Oct 22, 2017

@author: lloyd
'''
import random

class Actor(object):
    
    baseStat = 5.0
    baseHealth = 20.0
    baseMana = 20.0
    baseAttack = 5.0
    baseMagic = 5.0
    baseDefense = 2.0
    baseSpirit = 2.0
    
    healthConst = 5.0
    manaConst = 5.0
    attackConst = 1.0
    magicConst = 1.0
    defenseConst = 1.0
    spiritConst = 1.0
    
    statMods = {
        
        "warrior":[2.0, 1.0, 0.5],
        "cleric":[1.0, 0.5, 1.5],
        "wizard":[0.2, 0.5, 2.0],
        "monster":[1.0, 1.0, 1.0]
        }
    
    def __init__(self, name, job, gold):
        self.name = name
        self.job = job
        self.power = 1.0 # this is for monster use only
        self.strength = int(Actor.baseStat * self.getStatMod(0) * self.power)
        self.dexterity = int(Actor.baseStat * self.getStatMod(1) * self.power)
        self.intellect = int(Actor.baseStat * self.getStatMod(2) * self.power)
        self.maxHealth = self.calculateHealth()
        self.maxMana = self.calculateMana()
        
        self.attack = self.calculateAttack()
        self.magic = self.calculateMagic()
        self.defense = self.calculateDefense()
        self.spirit = self.calculateSpirit()
        
        self.health = self.maxHealth
        self.mana = self.maxMana
        self.gold = gold
        

    def calculateAttack(self):
        return self.strength * Actor.attackConst + Actor.baseAttack 
    
    def calculateMagic(self):
        return self.intellect * Actor.magicConst + Actor.baseMagic
    
    def calculateDefense(self):
        return self.dexterity * Actor.defenseConst + Actor.baseDefense
    
    def calculateSpirit(self):
        return self.intellect * Actor.spiritConst + Actor.baseSpirit
    
    def calculateHealth(self):
        return self.strength * Actor.healthConst + Actor.baseHealth
    
    def calculateMana(self):
        return self.intellect * Actor.manaConst + Actor.baseMana
    
    def getStatMod(self, statId):
        myJob = self.job.lower()
        return Actor.statMods[myJob][statId]
            
    def checkHp(self, amount):
        return self.health >= amount
       
    def adjustHp(self, amount):
        self.health += amount
        if self.health > self.maxHealth:
            self.health = self.maxHealth
        elif self.health < 0:
            self.health = 0
            self.death()
    
    def death(self):
        print("%s has perished!" % self.name)
        
    def printOutput(self, target, output):
        print("%s attacks %s for %i damage." % (self.name, target.name, output))
        
class Player(Actor):
    
    def __init__(self, name, job, gold):
        Actor.__init__(self, name, job, gold) 
        
    def adjustGold(self, amount):
        self.gold += amount
           
    def checkGold(self, amount):
        return self.gold >= amount
    
    def attackTarget(self, target):
        rng = random.randint(1,1000)
        output = 0
        if rng < 100:
            output = target.defense - self.attack * 2
        else:
            output = target.defense - self.attack
        
        self.printOutput(target, abs(output))
        target.adjustHp(output)
    
    def scanTarget(self, target):
        print(target.name + ":")
        print("Strength: " + target.strength + " Dexterity: " + target.dexterity + " Intellect: " + target.intellect)
        print("Attack: " + target.attack + " Magic: " + target.magic)
        print("Defense: " + target.defense + " Spirit: " + target.spirit)
        
        
class Mob(Actor):
    
    def __init__(self, name, power, gold):
        Actor.__init__(self, name, "monster", gold)
        self.power = power
        
    def aiScript(self, target):
        rng = random.randint(1,1000)
        output = 0
        if rng < 250:
            output = target.defense - self.attack * 2
        else:
            output = target.defense - self.attack
            
        self.printOutput(target, abs(output))
        target.adjustHp(output)
        