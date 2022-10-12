from src.Player import Player as Player
class Game:
    def __init__(self):
        self.__name = "MadZork"
        self.__version = "0.1"
        self.__author = "Mad Sharcky"
        self.__description = "MadZork is a text adventure game."
        self.__license = "MIT"
        self.__playerClass = ""
        self.__attackCount = 0
        self.__finished = False
        self.__finished = False
        self.__retreat = False
        self.__currentEnemy = None

        self.printWelcome()
        while self.__playerClass == "":
            self.__selectClass()
        self.__player = Player(self.__playerClass)

    def __selectClass(self):        
        print("")
        print("Select a class:")
        print("1. Warrior")
        print("2. Mage")
        print("3. Thief")
        match (input("> ")):
            case "1" | "Warrior" | "warrior":
                print("You are a Warrior!")
                self.__playerClass = "Warrior"
            case "2" | "Mage" | "mage":
                print("You are a Mage!")
                self.__playerClass = "Mage"
            case "3" | "Thief" | "thief":
                print("You are a Thief!")
                self.__playerClass = "Thief"
            case _:
                print("Invalid class.")     
                self.__playerClass = ""               


    def printWelcome(self):
        print("Welcome to " + self.__name + "!")
        print(self.__description)
        print("Version: " + self.__version)
        print("Author: " + self.__author)
        print("License: " + self.__license)
        print("Press any key to continue...")
        input()


    def play(self):
        while (not self.__finished):
            print("You are in a room.")
            print("What do you do?")
            command = input("> ")
            if (command == "quit"):
                self.__finished = True
        print("Thanks for playing!")