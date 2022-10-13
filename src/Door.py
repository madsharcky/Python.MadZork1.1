from utils.GeneralFunction import makeDiceRoll
class Door:
    def __init__(self):
        self._locked = False
        self._visible = True
        self._name = "Standard Door"
    def _isLocked(self):
        return self._locked
    def _isVisible(self):
        return self._visible
    def _openDoor(self):
        self._locked = False
    def _closeDoor(self):
        self._locked = True
        
class TrapDoor(Door):
    def __init__(self):
        super().__init__()
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
    def __init__(self):
        super().__init__()
        self._name = "Standard Door"
class LockedDoor(Door):
    def __init__(self):
        super().__init__()
        self._name = "Locked Door"
        self._locked = True
class SecretDoor(Door):
    def __init__(self):
        super().__init__()
        self._name = "Secret Door"
        self._visible = False