from utils.GeneralFunction import getListofChildClasses
from src.Player import Player
import IO.IO as IO
from resources.ClassNamesAndDescriptions import classNamesAndDescriptions
from os import name, system

def selectClass():
    playerClass = None
    classList = getListofChildClasses(Player)
    while playerClass == None:
        system('cls' if name == 'nt' else 'clear')
        print("Select a class:")
        for cls in classList:
            print(str(classList.index(cls)+1), ". ", cls.__name__)
        selection = input(">")
        if selection.isdigit() and int(selection) <= len(classList) and int(selection) > 0:
            playerClass = classList[int(selection)-1]()
            print("You selected the class: ", playerClass._name)
            print(classNamesAndDescriptions[playerClass._name])
            print ("Are you sure you want to select this class? (y/n)")
            if input(">") != "y":
                playerClass = None            
        else:
            print("Invalid input.")
    return playerClass
def printWelcome(game):
    system('cls' if name == 'nt' else 'clear')
    print("Welcome to " + game._name + "!")
    print(game._description)
    print("Version: " + game._version)
    print("Author: " + game._author)
    print("Press any key to continue...")
    input()
def printPlayerStats(player):
    xpRemaining = player.getXpToLevelUp() - player.getXp()
    output = "Level: " + str(player.getLevel())
    output += "\tXP: " + str(player.getXp()) + "/" + str(player.getXpToLevelUp()) + " (" + str(xpRemaining) + " remaining)"
    output += "\tHealth: " + str(player.getHealth()) + "/" + str(player.getMaxHealth())
    output += "\tAttack: " + str(player.getAtackChance())
    output += "\tDefense: " + str(player.getEvasion())
    output += "\tCarry Capacity: " + str(player.getCarryAmount()) + "/" + str(player.getCarryCapacity())
    output += "\tMoney: " + str(player.getMoney())
    print(output)
    print("")
def printStanding(game):
    system('cls' if name == 'nt' else 'clear')
    printPlayerStats(game._player)
    print("You are a", game._player.getName(), "and standing", game._currentRoom.getDescription())
    print(game._currentRoom.getDirections())
    print("What do you do?")
    command = IO.getCommandFromUserInput()
    return command

def executeCommand(command, game):
    if command.__contains__("quit"):
        print ("Are you sure you want to quit the game? (y/n)")
        if input(">").lower() == "y" or input(">") == "yes":
            game._finished = True
    else:
        for word in command:
            if word == "go":
                pass
            if word == "help":
                pass
            if word == "inventory":
                pass
            if word == "map":
                pass
            if word == "look":
                pass
            if word == "explore" or word == "search" or word == "examine":
                pass
            if word == "attack":
                pass
            if word == "take":
                pass
            if word == "drop":
                pass
            if word == "use":
                pass
            if word == "drink":
                pass
            if word == "open":
                pass
            if word == "close":
                pass
            if word == "kick" or word == "punch" or word == "hit" or word == "attack" or word == "fight" or word == "kill" or word == "stab":
                pass
            if word == "run" or word == "flee" or word == "retreat":
                pass
            
            
        
    print("Press any key to continue...")
    input()
    
