import random
import Item as ItemFile

def getRandomChildClass(parentClass):
    listOfChildClasses = [cls for cls in parentClass.__subclasses__()]
    return random.choice(listOfChildClasses)

item = ItemFile.Gold()
randomItem = getRandomChildClass(ItemFile.Item)
print(item.getDescription())
# print(randomItem.getDescription())