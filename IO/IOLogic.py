from utils.GeneralFunction import getListofChildClasses
from src.Player import Player
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