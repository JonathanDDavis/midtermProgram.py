#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jd0919889
#
# Created:     03/10/2019
# Copyright:   (c) jd0919889 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import time
import random
import sys

## delclare all varibles
prompt = "\n>> "
inventory = []

playerStats = {
    "strength" : 10,
    "dexterity" : 10,
    "constitution" : 10,
    "intelligence" : 10,
    "wisdom" : 10,
    "charisma" : 10,
    }

class player:
    def _init_(self, name, race, position, stats, health, alive):
        self.name = ""
        self.race = ""
        self.position = ""
        self.stats = playerStats
        self.stats = 100
        self.alive = True

def invalidInput():
    delayPrint("\nInvalid Input")

def delayPrint(x):
    for i in x:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.05)

def d4():
    roll = random.randrange(1,5)
    print(roll)

def d6():
    roll = random.randrange(1,7)
    print(roll)

def d8():
    roll = random.randrange(1,9)
    print(roll)

def d10():
    roll = random.randrange(1,11)
    print(roll)

def d12():
    roll = random.randrange(1,13)
    print(roll)

def d20():
    roll = random.randrange(1,21)
    print(roll)

## Need to work on this. Makes it were it will roll mulitply dice.
def sR1(w, x, y, z):
    sum(d6(), d6(), d6(), d6())
def sR2(w, x, y, z):
    sum(d6(), d6(), d6(), d6())
def sR3(w, x, y, z):
    sum(d6(), d6(), d6(), d6())
def sR4(w, x, y, z):
    sum(d6(), d6(), d6(), d6())
def sR5(w, x, y, z):
    sum(d6(), d6(), d6(), d6())
def sR6(w, x, y, z):
    sum(d6(), d6(), d6(), d6())

class warrior:
    def _init_(self, armor, weapons):
        self.armor = warriorArmor
        self.weapons = warriorWeapons

warriorWeapons[shortSword]
warriorArmor[]

shortSword{
    damage : 4
    }
class mage:
    def _init_(self, armor, weapons):
        self.armor = mageArmor
        self.weapons = mageWeapons

mageArmor[]
mageWeapons[fireWand]

fireWand{
    damage : 2
    burn : 1
    }
class human:
    def _init_(self, statsBoost):
        self.statsBoost = humanStatsBoost

class dwarf:
    def _init_(self, statsBoost):
        self.statsBoost = dwarfStatsBoost

print("Welcome to #insertNameOfGameHere")
print("What is your name")
player.name = input(prompt)
print("It is nice to meet you " + name)
ready = False
while ready == False:
    print("Are you ready to play" + player.name + "?")
    choice = input(prompt).lower()
    if choice == "yes":
        print("Great we will start.")
        ready = True
    elif choice == "no":
        print("Just tell when you are ready then.")
    else:
        invalidInput()

## Getting the race of the character
print("Okay time to create your character.")
print("What race would you want to be? (Human or Dwarf")
pickedRace = False
while pickedRace == False:
    choice = input(prompt).lower()
    if choice == "human":
        print("You are a human")
        player.race = "human"
        pickedRace = True
    elif choice == "dwarf":
        print("You are a dwarf")
        player.race = "dwarf"
        pickedRace = True
    else:
        invalidInput()

##Getting the class of the character
print("Now what do you want your class to be? (mage or warrior")
pickedClass = False
while pickedClass == False:
    choice = input(prompt).lower()
    if choice == "mage":
        print("You are a mage")
        player.position = "mage"
        pickedClass = True
    elif choice == "warrior":
        print("You are a warrior")
        player.position = "warrior"
        pickedClass = True
    else:
        invalidInput()

##Getting the stats for the character NEEDS LOT OF WORK
statRolls = False
while statRolls == False:
    print("Now it's time to get your stats.")
    sR1()
    sR2()
    sR3()
    sR4()
    sR5()
    sR6()
    print("Which one of these do you want to be your strength")
    choice = input(prompt)
    stats["strength"] = choice
    print("Which one of these do you want to be your dexterity")
    choice = input(prompt)
    stats["dexterity"] = choice
    print("Which one of these do you want to be your constitution")
    choice = input(prompt)
    stats["constitution"] = choice
    print("Which one of these do you want to be your intelligence")
    choice = input(prompt)
    stats["intelligence"] = choice
    print("Which one of these do you want to be your wisdom")
    choice = input(prompt)
    stats["wisdom"] = choice
    print("Which one of these do you want to be your charisma")
    choice = input(prompt)
    stats["charisma"] = choice


## The start of the game
newGame = True
while newGame == True
    print("You wake up and the first thing you see is that you are in a dark room. You try to move your arms but you find out that they are tied. You can tell that who ever tied you up used rope.")
    print("Do you want to try and break the rope?")
    free = False
    while free == False:
        choice = input(prompt).lower()
        if choice == "yes":
            if player.stats["strength"] >= 12:
                print("You use all of your strenth to try and rip the rope apart and the you hear a 'rip'. You broke the rope.")
                print("You look around the room a little and you can slightly see around the room now.")
                print("You see a short sword and a wand. Which one do you want to pick up")
                playerchoice = input(prompt).lower()
                if playerchoice == "short sword" or if playerchoice == "sword"

                free = True
            elif player.stats["strength"] < 12:
                print("You tried to break the rope but you can't. You strugled to get out of them but no matter what you do you couldn't get out.")
                print("You with you wrists slightly burnet from the rope. Someone walks into the room. He is a goblin. He has a cut over his left I and he and he is a little bit taller then you sitting on the ground.")
                print("He walks up to you and gets you to your feet and takes you out the door.")
            else:
                print("Check the code")
        elif choice == "no":
            print("You don't try to break out. You sit there waiting to see who captured you")
        else:
            invalidInput()
    print("You walk out of the room and you can go either left or right? Which way would you want to go?")






























