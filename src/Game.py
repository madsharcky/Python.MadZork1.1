from src.Player import Player as Player
from src.Player import selectClass
class Game:
    def __init__(self):
        self.__name = "MadZork"
        self.__version = "0.1"
        self.__author = "Mad Sharcky"
        self.__description = "MadZork is a text adventure game."
        self.__playerClass = ""
        self.__attackCount = 0
        self.__finished = False
        self.__retreat = False
        self.__currentEnemy = None

        self.printWelcome()
        self.__player = selectClass()() #adittional () to initialize the class


    def printWelcome(self):
        print("Welcome to " + self.__name + "!")
        print(self.__description)
        print("Version: " + self.__version)
        print("Author: " + self.__author)
        print("Press any key to continue...")
        input()


    def play(self):
        while (not self.__finished):
            print("You are a", self.__player.getName(), "and standing in a room.")
            print("What do you do?")
            command = input("> ")
            if (command == "quit"):
                self.__finished = True
        print("Thanks for playing!")