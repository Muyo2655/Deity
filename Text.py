'''
Created on Oct 24, 2017

@author: lloyd
'''

options = ("[1] ","[2] ","[3] ","[4] ","[5] ")

choose = ("Yes","No")

generic = (" ", "Leave Conversation","You can't afford that!")

newMenu = ("Start", "Load", "Exit")

newGame = (
    "I don't really know what to do; can you help me? (Tutorial)",
    "Any news?",
    "Point me in the direction of the nearest bar room brawl!",
    "I need a drink.",
    "Innkeeper: What is your name, traveler?",
    "Innkeeper: What kind of adventurer are you?",
    "Warrior",
    "Cleric",
    "Wizard",
    "Innkeeper: I'm sure I've heard that name before.",
    "You are standing inside a bustling pub.  The innkeeper is eyeing you, and you don't know\nif it's true that he knows you or is simply weary of your presence.",
    "If you change your mind, let me know.",
    "Have this; it will make you feel better."
)

battle = (
    "Attack",
    "Scan",
    "You lose!  You lose half of your gold."
)

elements = ("Fire", "Water", "Shock", "Pierce", "Blunt", "Slash")

def yesNo():
    for i in range(0, 2):
        print(options[i] + choose[i])
