#TODO
# room.addItem(item)
# room.getItems()
# room.removeItem(item)
from resources.RoomDescriptions import getRandomDescription
from utils.GeneralFunction import getRandomChildClass
import src.Item as ItemFile
def listOfChildClassesItem(file):
    classes = dir(file)
    items = []
    for method in classes:
        if method.startswith("__"):
            continue
        if method == "Item":
            continue
        else:
            items.append(method)
    return items



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
        pass
    def __makeItems(self):
        if not self.__player.hasKeys():
            self.__items.append(ItemFile.Key())
        if self.__player.getHealth() < self.__player.getMaxHealth()*0.75:
            self.__items.append(getRandomChildClass(ItemFile.Item)())
        if self.__player.getHealth() < self.__player.getMaxHealth()*0.5:
            self.__items.append(getRandomChildClass(ItemFile.Item)())
        if self.__player.getHealth() < self.__player.getMaxHealth()*0.25:
            self.__items.append(getRandomChildClass(ItemFile.Item)())
        
    def __makeDoors(self):
        pass
    