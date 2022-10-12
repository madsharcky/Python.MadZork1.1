import random

class Item:
    def __init__(self):
        self.__name = ""
        self.__description = ""
        self.__weight = 0
        self.__value = 0
        self.__power = 0
        self.__isMoney = False
    def getValue(self):
        return self.__value
    def getPower(self):
        return self.__power
    def isMoney(self):
        return self.__isMoney
    def getWeight(self):
        return self.__weight
    def getName(self):
        return self.__name
    def getDescription(self):
        return self.__description    
    def __str__(self):        
        return self.__name + ": " + self.__description

class Key(Item):
    def __init__(self):
        super().__init__()
        self.__name = "Key"
        self.__description = "A simple key to open locked doors."
        self.__weight = 1
        self.__value = 0
        self.__power = 0
        self.__isMoney = False
class Potion(Item):
    def __init__(self):
        super().__init__()
        self.__name = "Potion"
        self.__description = "A potion to heal wounds. Restores 50 health."
        self.__weight = 1
        self.__value = 0
        self.__power = 50
        self.__isMoney = False
class Bronze(Item):
    def __init__(self):
        super().__init__()
        self.__name = "Bronze"
        self.__description = "A bronze coin worth 100 money."
        self.__weight = 0
        self.__value = 100
        self.__power = 0
        self.__isMoney = True
class Silver(Item):
    def __init__(self):
        super().__init__()
        self.__name = "Silver"
        self.__description = "A silver coin worth 200 money."
        self.__weight = 0
        self.__value = 200
        self.__power = 0
        self.__isMoney = True
class Gold(Item):
    def __init__(self):
        super().__init__()        
        self.__name = "Gold"
        self.__description = "A gold coin worth 500 money."
        self.__weight = 0
        self.__value = 500
        self.__power = 0
        self.__isMoney = True

#TODO make inheritance work

def getRandomChildClass(parentClass):
    listOfChildClasses = [cls for cls in parentClass.__subclasses__()]
    return random.choice(listOfChildClasses)

item = Gold()
print("Item description: ", item.getDescription())
randomItem = getRandomChildClass(Item)
# print(randomItem.getDescription())