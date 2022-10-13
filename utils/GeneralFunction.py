import random

def getListofChildClasses(parentClass):
    return [cls for cls in parentClass.__subclasses__()]

def getRandomChildClass(parentClass):
    listOfChildClasses = [cls for cls in parentClass.__subclasses__()]
    return random.choice(listOfChildClasses)()

def makeDiceRoll(minValue = 1, nrOfSides = 20):
        return random.randint(minValue, nrOfSides)
    
def getDirectionFromInt(direction):
    if direction == 0:
        return "north"
    elif direction == 1:
        return "east"
    elif direction == 2:
        return "south"
    elif direction == 3:
        return "west"
    else:
        return "error"