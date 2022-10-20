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
        self._player = IOLogic.selectClass()
        self._currentRoom = Room(self._player)


    def play(self):
        while (not self._finished):
            command = IOLogic.printStanding(self)
            IOLogic.executeCommand(command, self)
        print("Thanks for playing!")