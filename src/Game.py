from os import system, name
from src.Player import Player as Player
from src.Player import selectClass
from src.Room import Room
class Game:
    def __init__(self):
        self.__name = "MadZork"
        self.__version = "0.1"
        self.__author = "Mad Sharcky"
        self.__description = "MadZork is a text adventure game."
        self.__attackCount = 0
        self.__finished = False
        self.__retreat = False
        self.__currentEnemy = None

        self.printWelcome()
        self.__player = selectClass()
        self.__currentRoom = Room(self.__player)


    def printWelcome(self):
        system('cls' if name == 'nt' else 'clear')
        print("Welcome to " + self.__name + "!")
        print(self.__description)
        print("Version: " + self.__version)
        print("Author: " + self.__author)
        print("Press any key to continue...")
        input()


    def play(self):
        while (not self.__finished):
            system('cls' if name == 'nt' else 'clear')
            print("You are a", self.__player.getName(), "and standing in a room.")
            print(self.__currentRoom.getDirections())
            print("What do you do?")
            command = input(">")
            if (command == "quit"):
                self.__finished = True
        print("Thanks for playing!")