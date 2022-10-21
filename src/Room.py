#TODO
# room.addItem(item)
# room.getItems()
# room.removeItem(item)
from resources.RoomDescriptions import getRandomDescription
from utils.GeneralFunction import getDirectionFromInt, getRandomChildClass, makeDiceRoll
import src.Item as ItemFile
import src.Enemy as EnemyFile
import src.Door as DoorFile

class Room:
    def __init__(self, player):
        self.__player = player
        self.__description = getRandomDescription()
        self.__items = []
        self.__doors = {}
        self.__enemies = []
        self.__visited = False 
        self.__explored = True #TODO change back to false
        self.__firstTimeHere = True
        self.__makeEnemies()
        self.__makeItems()
        self.__makeDoors()

    def __makeEnemies(self):
        maxAmount = 1
        if self.__player.getHealth() > self.__player.getMaxHealth()*0.25:
            maxAmount += 1
        if self.__player.getHealth() > self.__player.getMaxHealth()*0.5:
            maxAmount += 1
        if self.__player.getHealth() > self.__player.getMaxHealth()*0.75:
            maxAmount += 1      
        randomAmount = makeDiceRoll(0, maxAmount)  
        for i in range(1, makeDiceRoll(0, maxAmount)):
            self.__enemies.append(getRandomChildClass(EnemyFile.Enemy)(self.__player))
    def __makeItems(self):
        maxAmount = 1
        if not self.__player.hasKeys():
            self.__items.append(ItemFile.Key())
        if self.__player.getHealth() < self.__player.getMaxHealth()*0.75:
            maxAmount += 1
        if self.__player.getHealth() < self.__player.getMaxHealth()*0.5:
            maxAmount += 1
        if self.__player.getHealth() < self.__player.getMaxHealth()*0.25:
            maxAmount += 1
        randomAmount = makeDiceRoll(0, maxAmount)
        for i in range(1, makeDiceRoll(0, maxAmount)):
            self.__items.append(getRandomChildClass(ItemFile.Item)())
    def __makeDoors(self):
        self.__doors = {
            "north": None,
            "east": None,
            "south": None,
            "west": None
        }
        for i in range(4):
            if makeDiceRoll(1, 100) > 50:
                self.__doors[getDirectionFromInt(i)] = getRandomChildClass(DoorFile.Door)()
    def getDescription(self):
        return self.__description
    def getItems(self):
        return self.__items
    def getDoor(self, direction):
        return self.__doors[direction]
    def getEnemies(self):
        return self.__enemies
    def getVisited(self):
        return self.__visited
    def getExplored(self):
        return self.__explored
    def getFirstTimeHere(self):
        return self.__firstTimeHere
    def getRandomEnemy(self):
        if len(self.__enemies) > 0:
            return self.__enemies[makeDiceRoll(len(self.__enemies))-1]
        else:
            return None
    def getDirections(self):
        returnString = ""
        if self.__explored:
            returnString = "You see no doors."
            nrOfExits = 0            
            for direction in self.__doors:
                if self.__doors[direction] != None:
                    if self.__doors[direction]._isVisible:  # type: ignore
                        nrOfExits += 1
            if nrOfExits > 0:
                returnString = "The doors you see are to the:"
                for direction in self.__doors:
                    if self.__doors[direction] != None:
                        if self.__doors[direction]._isVisible:  # type: ignore
                            returnString += "\n" + direction            
        else:
            returnString = "You dont know this room. You need to explore it first"
        return returnString
    def killEnemy(self, enemy):
        self.__enemies.remove(enemy)
    def removeItem(self, item):
        self.__items.remove(item)
    def setVisited(self, visited):
        self.__visited = visited
    def setExplored(self, explored):
        self.__explored = explored
    def setFirstTimeHere(self, firstTimeHere):
        self.__firstTimeHere = firstTimeHere
    def recieveItem(self, item):
        self.__items.append(item)