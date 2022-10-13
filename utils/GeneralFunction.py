from random import randint, random

def getListofChildClasses(parentClass):
    return [cls for cls in parentClass.__subclasses__()]

def getRandomChildClass(parentClass):
    listOfChildClasses = [cls for cls in parentClass.__subclasses__()]
    return random.choice(listOfChildClasses)()

def makeDiceRoll(minValue = 1, nrOfSides = 20):
        return randint(minValue, nrOfSides)