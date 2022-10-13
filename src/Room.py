#TODO
# room.addItem(item)
# room.getItems()
# room.removeItem(item)
from resources.RoomDescriptions import getRandomDescription
from utils.GeneralFunction import getRandomChildClass
from utils.GeneralFunction import makeDiceRoll
import src.Item as ItemFile
import src.Enemy as EnemyFile


class Room:
    def __init__(self, player):
        self.__player = player
        self.__description = getRandomDescription()
        self.__items = []
        self.__exits = {}
        self.__enemies = []
        self.__visited = False
        self.__explored = False
        self.__firstTimeHere = True
        self.__makeEnemies()
        self.__makeItems()
        self.__makeDoors()

    def __makeEnemies(self):
        maxAmount = 0
        if self.__player.getHealth() < self.__player.getMaxHealth()*0.25:
            maxAmount += 1
        if self.__player.getHealth() < self.__player.getMaxHealth()*0.5:
            maxAmount += 1
        if self.__player.getHealth() < self.__player.getMaxHealth()*0.75:
            maxAmount += 1        
        for i in range(1, makeDiceRoll(0, maxAmount)):
            self.__enemies.append(getRandomChildClass(EnemyFile.Enemy)())
    def __makeItems(self):
        maxAmount = 0
        if not self.__player.hasKeys():
            self.__items.append(ItemFile.Key())
        if self.__player.getHealth() < self.__player.getMaxHealth()*0.75:
            maxAmount += 1
        if self.__player.getHealth() < self.__player.getMaxHealth()*0.5:
            maxAmount += 1
        if self.__player.getHealth() < self.__player.getMaxHealth()*0.25:
            maxAmount += 1
        for i in range(1, makeDiceRoll(0, maxAmount)):
            self.__items.append(getRandomChildClass(ItemFile.Item)())
    def __makeDoors(self):
        pass
    