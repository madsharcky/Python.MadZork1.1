
class Item:
    def __init__(self):
        self._name = "Standard Item"
        self._description = "Standard Item Description"
        self._weight = 0
        self._value = 0
        self._power = 0
        self._isMoney = False
    def getValue(self):
        return self._value
    def getPower(self):
        return self._power
    def isMoney(self):
        return self._isMoney
    def getWeight(self):
        return self._weight
    def getName(self):
        return self._name
    def getDescription(self):
        return self._description    
    def _str_(self):        
        return self._name + ": " + self._description

class Key(Item):
    def __init__(self):
        super().__init__()
        self._name = "Key"
        self._description = "A simple key to open locked doors."
        self._weight = 1
        self._value = 0
        self._power = 0
        self._isMoney = False
class Potion(Item):
    def __init__(self):
        super().__init__()
        self._name = "Potion"
        self._description = "A potion to heal wounds. Restores 50 health."
        self._weight = 1
        self._value = 0
        self._power = 50
        self._isMoney = False
class Bronze(Item):
    def __init__(self):
        super().__init__()
        self._name = "Bronze"
        self._description = "A bronze coin worth 100 money."
        self._weight = 0
        self._value = 100
        self._power = 0
        self._isMoney = True
class Silver(Item):
    def __init__(self):
        super().__init__()
        self._name = "Silver"
        self._description = "A silver coin worth 200 money."
        self._weight = 0
        self._value = 200
        self._power = 0
        self._isMoney = True
class Gold(Item):
    def __init__(self):
        super().__init__()       
        self._name = "Gold"
        self._description = "A gold coin worth 500 money."
        self._weight = 0
        self._value = 500
        self._power = 0
        self._isMoney = True
