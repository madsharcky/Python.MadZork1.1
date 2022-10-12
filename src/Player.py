class Player:
    def __init__(self, playerClass):
        self.playerClass = playerClass
        match self.playerClass:
            case "Warrior":
                self.maxhelath = 20
                self.attack = 2
                self.defense = 2
                self.carryCapacity = 2
            case "Mage":
                self.maxhelath = 10
                self.attack = 4
                self.defense = 1
                self.carryCapacity = 1 
            case "Thief":
                self.maxhelath = 15
                self.attack = 3
                self.defense = 1
                self.carryCapacity = 2
        self.level = 1        
        self.health = self.maxhealth
        self.keys = 0
        self.money = 0
        self.potions = 0
        self.monstersKilled = 0
        self.keysUsed = 0
        self.potionsUsed = 0
        self.walkedInWalls = 0
        self.roomsExplored = 0
        self.itemsPickedUp = 0
        self.itemsDropped = 0
        self.damageDealt = 0
        self.damageTaken = 0
        self.itemWasGiven = False
