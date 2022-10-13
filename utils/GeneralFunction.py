from random import randint, random


def getRandomChildClass(parentClass):
    listOfChildClasses = [cls for cls in parentClass.__subclasses__()]
    return random.choice(listOfChildClasses)()

def makeDiceRoll(nrOfSides = 20):
        return randint(1, nrOfSides)