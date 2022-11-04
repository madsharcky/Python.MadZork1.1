from utils.GeneralFunction import makeDiceRoll
class Door:
    def __init__(self, creatorRoom):
        self._creatorRoom = creatorRoom
        self._nextRoom = None
        self._locked = False
        self._visible = True
        self._name = "Parent Door"
    def _isLocked(self):
        return self._locked
    def _isVisible(self):
        return self._visible
    def _openDoor(self):
        self._locked = False
    def _closeDoor(self):
        self._locked = True
    def _getName(self):
        return self._name
    def gothroughDoor(self, player):
        if self._locked:
            return "locked"
        elif self._name == "Trap Door":
            return "trap"
        elif player.hasCrossedDoor(self):
            return "crossed"
        else:
            return "normal"
    def goThroughDoor(self, player):
        player.crossDoor(self)
        if self._nextRoom == None:
            return "trap"
        
        
class TrapDoor(Door):
    def __init__(self, creatorRoom):
        super().__init__(creatorRoom)
        self._name = "Trap Door"
        self._attackChance = makeDiceRoll()
        self.__damage = makeDiceRoll(10)
    def _attackEnemy(self):
        diceRoll = makeDiceRoll()
        if diceRoll == 20:
            return (self._attackChance * 2) + diceRoll
        elif diceRoll == 1:
            return 0
        else:
            return self._attackChance + diceRoll
    def makeDamage(self):
        return self.__damage
class StandardDoor(Door):
    def __init__(self, creatorRoom):
        super().__init__(creatorRoom)
        self._name = "Standard Door"
class LockedDoor(Door):
    def __init__(self, creatorRoom):
        super().__init__(creatorRoom)
        self._name = "Locked Door"
        self._locked = True
class SecretDoor(Door):
    def __init__(self, creatorRoom):
        super().__init__(creatorRoom)
        self._name = "Secret Door"
        self._visible = False