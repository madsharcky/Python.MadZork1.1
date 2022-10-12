#TODO
# room.addItem(item)
# room.getItems()
# room.removeItem(item)
from resources.RoomDescriptions import getRandomDescription

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

    def __makeEnemies():        
        pass
    def __makeItems():
        pass
    def __makeDoors():
        pass
    