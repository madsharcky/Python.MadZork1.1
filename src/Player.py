from utils.GeneralFunction import makeDiceRoll
from resources.ClassNamesAndDescriptions import classNamesAndDescriptions

class Player:
    def __init__(self):
        self._maxhealth = 100
        self._attackChance = 1
        self._evasion = 1
        self._carryCapacity = 1                  
        self._damage = 1
        self._level = 1        
        self._xp = 0
        self._health = self._maxhealth
        self._money = 0
        self._items = []
        self._name = "Player"
        self._description = classNamesAndDescriptions[self._name]
        # Stats
        self.monstersKilled = 0
        self.keysUsed = 0
        self.potionsUsed = 0
        self.walkedInWalls = 0
        self.roomsExplored = 0
        self.itemsPickedUp = 0
        self.itemsDropped = 0
        self.damageDealt = 0
        self.damageTaken = 0
        self.alcoholSips = 0
        # States
        self.isFighting = False
        self._crossedDoors = []
        
    def crossDoor(self, door):
        if self._crossedDoors.__contains__(door):
            self._crossedDoors.__delitem__(self._crossedDoors.index(door))
        else:
            self._crossedDoors.append(door)
    def getIsFighting(self):
        return self.isFighting    
    def _levelUp(self):
        self._level += 1
        self._xp -= self._xpToLevelUp()
        if self._xp < 0:
            self._xp = 0
        invalidInput = True
        while invalidInput:
            print("You leveled up! You are now level ", self._level ,". Select a stat to increase:")
            print("1. Health")
            print("2. Attackchance")
            print("3. Evasion")
            print("4. Carry Capacity")
            stat = input("> ")
            match stat:
                case "1" | "Health" | "health":
                    self._health = (self._health / self._maxhealth) * self._maxhealth+10
                    self._maxhealth += 10
                    invalidInput = False
                case "2" | "Attack" | "attack" | "Attackchance" | "attackchance":
                    self._attackChance += 1
                    invalidInput = False
                case "3" | "Evasion" | "evasion":
                    self._evasion += 1
                    invalidInput = False
                case "4" | "Carry Capacity" | "carry capacity":
                    self._carryCapacity += 1
                    invalidInput = False
                case __:
                    print("Invalid input.")
        self._levelUpClassBonus()
    def _levelUpClassBonus(self): 
        pass # Implement in child classes
    def _calculateMoney(self):
        for item in self._items:
            if item.isMoney():
                self._money += item.getValue()
    def _xpToLevelUp(self):
        return self._level **2 + 99
    def _carryAmount(self):
        carryAmount = 0
        for item in self._items:
            if item.wieght != None:
                carryAmount += item.wieght
        return carryAmount
    def _getPotions(self):
        potions = []
        for item in self._items:
            if item.isPotion():
                potions.append(item)
        return potions
    def _getKeys(self):
        keys = []
        for item in self._items:
            if item.isKey():
                keys.append(item)
        return keys
    def getLevel(self):
        return self._level
    def getXp(self):
        return self._xp
    def getXpToLevelUp(self):
        return self._xpToLevelUp()
    def getAtackChance(self):
        return self._attackChance
    def getEvasion(self):
        return self._evasion
    def getCarryAmount(self):
        return self._carryAmount()
    def getCarryCapacity(self):
        return self._carryCapacity

    def hasKeys(self):
        if len(self._getKeys()) > 0:
            return True
        else:
            return False
    def getMoney(self):
        return self._money
    def dropItem(self, item, room):        
        if item in self._items:
            self._items.remove(item) #TODO Check if all items are droped or only one
            room.addItem(item)
            self.itemsDropped += 1
            self._calculateMoney()
            return True
        else:
            return False
    def pickUpItem(self, item, room):
        if self._carryAmount() < self._carryCapacity:
            if item in room.getItems():
                room.removeItem(item)
                self._items.append(item)
                self.itemsPickedUp += 1
                self._calculateMoney()
                return True
            else:
                return False
        else:
            return False
    def drinkPotion(self):
        if len(self._getPotions()) > 0:
            self._items.remove(self._getPotions()[0])
            self._health += self._getPotions()[0].getPower()
            if self._health > self._maxhealth:
                self._health = self._maxhealth
            self.potionsUsed += 1
            return True
        else:
            return False
    def giveXp(self, xp):
        self._xp += xp
        if self._xp >= self._xpToLevelUp:            
            self._levelUp()
    def defend(self, atackChance):
        if makeDiceRoll() + self._evasion > atackChance:
            return True
        else:
            return False
    def attackEnemy(self):
        diceRoll = makeDiceRoll()
        if diceRoll == 20:
            return (self._attackChance* 2) + diceRoll
        elif diceRoll == 1:
            return 0
        else:
            return self._attackChance + diceRoll
    def takeDamage(self, damage):
        self._health -= damage
        self.damageTaken += damage
        if self._health <= 0:
            self._health = 0
            return False
        else:
            return True
    def makeDamage(self):
        return self._damage
    def getName(self):
        return self._name
    def getMaxHealth(self):
        return self._maxhealth
    def getHealth(self):
        return self._health
    
class Warrior(Player):
    def __init__(self):
        super().__init__()
        self._maxhealth = 100
        self._health = self._maxhealth
        self._attackChance = 2
        self._evasion = 1
        self._carryCapacity = 1
        self._damage = 1
        self._name = "Warrior"
    def _levelUpClassBonus(self):
        self._damage += 1
class Tank(Player):
    def __init__(self):
        super().__init__()
        self._maxhealth = 100
        self._health = self._maxhealth
        self._attackChance = 1
        self._evasion = 2
        self._carryCapacity = 2
        self._damage = 1
        self._name = "Tank"
    def _levelUpClassBonus(self):
        self._maxhealth += 10
class Assassin(Player):
    def __init__(self):
        super().__init__()
        self._maxhealth = 100
        self._health = self._maxhealth
        self._attackChance = 1
        self._evasion = 1
        self._carryCapacity = 1
        self._damage = 2
        self._name = "Assassin"
    def _levelUpClassBonus(self):
        self._evasion += 1
    
