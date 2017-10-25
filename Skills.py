'''
Created on Oct 25, 2017

@author: lloyd
'''
import com.lloyd.base.Formula as form
import com.lloyd.base.Utils as util

class Skill(object):
    
    def __init__(self, name, desc, power, hit, cost, element, level, magical, critChance, critMult):
        self.name = name
        self.description = desc
        self.power = power
        self.hit = hit
        self.cost = cost
        self.element = element
        self.level = level
        self.magical = magical
        self.critChance = critChance
        self.critMult = critMult
        
        self.output = 0
        
    def useSkill(self, caster, target):
        # set caster and target and reset crit/output
        self.caster = caster
        self.target = target
        self.critical = False
        self.output = 0
        # check if sufficient MP
        if self.checkMp():
        # cast spell
            if self.rollHit():
        # calculate output
                self.calculateOutput()
        # print output
                self.printOutput()
            else:
                self.printMiss()
        else:
            print("Insufficient MP!")
        
    def checkMp(self):
        return self.caster.mana >= self.cost
    
    def rollHit(self):
        return util.randomInt() <= (self.hit + self.caster.dexterity) * 100
    
    def calculateOutput(self):
        if self.magical:
            self.output = form.magicalFormula(self.caster, self.target, self)
        else:
            self.output = form.physicalFormula(self.caster, self.target, self)
        
        if self.rollCritical():
            self.critical = True
            self.output *= self.critMult
        
        if(self.output < 0):
            self.output = 0
        
        return self.output 
    
    def printOutput(self):
        print("%s casts %s on %s for %i %s damage." % (self.caster.name, self.name, self.target.name, self.output, self.element))
    
    def printMiss(self):
        print("%s casts %s on %s, but it misses!" % (self.caster.name, self.name, self.target.name))
          
    def rollCritical(self):
        return util.randomInt() <= (self.caster.dexterity * self.critChance) * 100
            