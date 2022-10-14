from os import system, name
from src.Player import Player as Player
import IO.IOLogic as IOLogic
from src.Room import Room
class Game:
    def __init__(self):
        self._name = "MadZork"
        self._version = "0.1"
        self._author = "Mad Sharcky"
        self._description = "MadZork is a text adventure game."
        self._attackCount = 0
        self._finished = False
        self._retreat = False
        self._urrentEnemy = None

        IOLogic.printWelcome(self)
        self.__player = IOLogic.selectClass()
        self.__currentRoom = Room(self.__player)


    def play(self):
        while (not self._finished):
            system('cls' if name == 'nt' else 'clear')
            print("You are a", self.__player.getName(), "and standing in a room.")
            print(self.__currentRoom.getDirections())
            print("What do you do?")
            command = input(">")
            if (command == "quit"):
                self.__finished = True
        print("Thanks for playing!")