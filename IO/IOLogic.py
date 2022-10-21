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
        if input(">").lower() == "y" or input(">").lower() == "yes":
            game._finished = True
    else:
        iterator = iter(command)
        for word in iterator:
            if word == "go":          
                direction = checkifWordIsDirection(next(iterator, None))
                if direction == None:
                    print("I do not know where you want to go.")                    
                else:
                    goToRoom(direction, game)
                pass
            elif word == "help":
                printHelp()
            elif word == "inventory":
                printInventory(game._player)
            elif word == "map":
                printMap()
            elif word == "look" or word == "explore" or word == "search" or word == "examine":
                exploreRoom(game._currentRoom)
            elif word == "take":
                pass
            elif word == "drop":
                pass
            elif word == "use":
                pass
            elif word == "drink":
                pass
            elif word == "open":
                pass
            elif word == "kick" or word == "punch" or word == "hit" or word == "attack" or word == "fight" or word == "kill" or word == "stab":
                pass
            elif word == "run" or word == "flee" or word == "retreat":
                pass
        print("Press any key to continue...")
        input()
    
def goToRoom(direction, game): #TODO complete this function
    pass
def checkifWordIsDirection(word):
    if word == None:
        return None
    elif word == "north" or word == "up":
        return "north"
    elif word == "south" or word == "down":
        return "south"
    elif word == "east" or word == "right":
        return "east"
    elif word == "west" or word == "left":
        return "west"
def printHelp():
    print("This is a list of accepted commands:")
    string = ""
    for word in IO.getValidUserInputs():
        string += word + ", "
    string = string[:-2]
    print(string)
def printInventory(player):
    print("You are carrying:")
    if len(player._items) == 0:
        print("Nothing")
    else:
        for item in player._items:
            print(item.getName())
def printMap(): #TODO complete this function
    pass
def exploreRoom(room): #TODO complete this function
    print ("All the Items in the room:")
    for item in room.getItems():
        print (item.getName())
    print("All the Enemies in the room:")
    for enemy in room.getEnemies():
        print(enemy.getName())
