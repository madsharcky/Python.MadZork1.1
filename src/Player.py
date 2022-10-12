from random import randint

class Player:
    def __init__(self, playerClass):
        match playerClass:
            case "Warrior":
                self.__maxhealth = 20
                self.__attack = 2
                self.__defense = 2
                self.__carryCapacity = 2
            case "Mage":
                self.__maxhealth = 10
                self.__attack = 4
                self.__defense = 1
                self.__carryCapacity = 1 
            case "Thief":
                self.__maxhealth = 15
                self.__attack = 3
                self.__defense = 1
                self.__carryCapacity = 2            
        self.__playerClass = playerClass
        self.__level = 1        
        self.__health = self.__maxhealth
        self.__money = 0
        self.__items = []
        self.__xp = 0
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
    
    def __levelUp(self):
        self.__level += 1
        self.__xp -= self.__xpToLevelUp
        if self.__xp < 0:
            self.__xp = 0
        invalidInput = True
        while invalidInput:
            print("You leveled up! You are now level ", self.__level ,". Select a stat to increase:")
            print("1. Health")
            print("2. Attack")
            print("3. Defense")
            print("4. Carry Capacity")
            stat = input("> ")
            match stat:
                case "1" | "Health" | "health":
                    self.__health = (self.__health / self.__maxhealth) * self.__maxhealth+10
                    self.__maxhealth += 10
                    invalidInput = False
                case "2" | "Attack" | "attack":
                    self.__attack += 1
                    invalidInput = False
                case "3" | "Defense" | "defense":
                    self.__defense += 1
                    invalidInput = False
                case "4" | "Carry Capacity" | "carry capacity":
                    self.__carryCapacity += 1
                    invalidInput = False
                case __:
                    print("Invalid input.")    
    def __makeDiceRoll(self, nrOfSides = 20):
        return randint(1, nrOfSides)
    def __calculateMoney(self):
        for item in self.__items:
            if item.isMoney():
                self.__money += item.getValue()
    def __xpToLevelUp(self):
        return self.__level **2 + 99
    def __carryAmount(self):
        carryAmount = 0
        for item in self.__items:
            if item.wieght != None:
                carryAmount += item.wieght
        return carryAmount
    def __getPotions(self):
        potions = []
        for item in self.__items:
            if item.isPotion():
                potions.append(item)
        return potions
    def __getKeys(self):
        keys = []
        for item in self.__items:
            if item.isKey():
                keys.append(item)
        return keys

    def hasKeys(self):
        if len(self.__getKeys) > 0:
            return True
        else:
            return False
    def getMoney(self):
        return self.__money
    def getHealth(self):
        return self.__health
    def dropItem(self, item, room):        
        if item in self.__items:
            self.__items.remove(item) #TODO Check if all items are droped or only one
            room.addItem(item)
            self.itemsDropped += 1
            self.__calculateMoney()
            return True
        else:
            return False
    def pickUpItem(self, item, room):
        if self.__carryAmount < self.__carryCapacity:
            if item in room.getItems():
                room.removeItem(item)
                self.__items.append(item)
                self.itemsPickedUp += 1
                self.__calculateMoney()
                return True
            else:
                return False
        else:
            return False
    def drinkPotion(self):
        if len(self.__getPotions) > 0:
            self.__items.remove(self.__getPotions[0])
            self.__health += self.__getPotions[0].getPower()
            if self.__health > self.__maxhealth:
                self.__health = self.__maxhealth
            self.potionsUsed += 1
            return True
        else:
            return False
    def giveXp(self, xp):
        self.__xp += xp
        if self.__xp >= self.__xpToLevelUp:            
            self.levelUp()
    def getStats(self):
        xpRemaining = self.__xpToLevelUp - self.__xp
        output = "Level: " + str(self.__level)
        output += "\tXP: " + str(self.__xp) + "/" + str(self.__xpToLevelUp) + " (" + str(xpRemaining) + " remaining)"
        output += "\tHealth: " + str(self.__health) + "/" + str(self.__maxhealth)
        output += "\tAttack: " + str(self.__attack)
        output += "\tDefense: " + str(self.__defense)
        output += "\tCarry Capacity: " + self.__carryAmount + "/" + str(self.__carryCapacity)
        output += "\tMoney: " + str(self.__money)
        return output
    def defend(self, enemyatack):
        if self.__makeDiceRoll() + self.__defense > enemyatack:
            return True
        else:
            return False
    def takeDamage(self, damage):
        self.__health -= damage
        self.damageTaken += damage
        if self.__health <= 0:
            self.__health = 0
            return False
        else:
            return True
    def attack(self):
        diceRoll = self.__makeDiceRoll()
        if diceRoll == 20:
            return self.__attack * 2
        elif diceRoll == 1:
            return 0
        else:
            return self.__attack
    