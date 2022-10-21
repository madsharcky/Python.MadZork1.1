from utils.GeneralFunction import makeDiceRoll

class Enemy:
    def __init__(self, player):
        self._player = player
        self._name = "Standard Enemy"
        self._description = "A standard enemy"
        self._level = self._player.getLevel()
        self._health = 1
        self._attackChance = 1
        self._defense = 1
        self._damage = 1
        self._firstAttack = True
        self._attackMove = ["It attacks you"]
    def _selectRandomAttackMove(self):
        return self._attackMove[makeDiceRoll(len(self._attackMove))-1]
    def _defend(self, enemyatack):
        if makeDiceRoll() + self._defense > enemyatack:
            return True
        else:
            return False
    def _attackEnemy(self):
        diceRoll = makeDiceRoll()
        if diceRoll == 20:
            return (self._attackChance * 2) + diceRoll
        elif diceRoll == 1:
            return 0
        else:
            return self._attackChance + diceRoll
    def _takeDamage(self, damage):
        self._health -= damage
        if self._health <= 0:
            self._health = 0
            return False
        else:
            return True
    def makeDamage(self):
        return self._damage
    def getName(self):
        return self._name
    def _getDescription(self):
        return self._description
    def _giveXP(self, roundsTillDeath):
        if self._level * (30 - roundsTillDeath) > 10:
            return self._level * (30 - roundsTillDeath)
        else :
            return 10
    def _getAttackMove(self):
        return "The ", self.getName, " runs toward you. ", self._getDescription, "\n", self._selectRandomAttackMove()
    
class OwlbearSkeleton(Enemy):
    def __init__(self, player):
        super().__init__(player)
        self._name = "Owlbear Skeleton"
        self._description = "A skeleton of an owlbear"
        self._health = self._level * 3
        self._attackChance = self._level
        self._defense = self._level
        self._damage = self._level
        self._attackMove = [
                "With its huge claws it wildly slashes in your direction",
                "It snaps at you with its peak",
                "It slams into you"
            ]
class WolfSkeleton(Enemy):
    def __init__(self, player):
        super().__init__(player)
        self._name = "Wolf Skeleton"
        self._description = "A skeleton of a Wolf"
        self._health = self._level * 10
        self._attackChance = self._level
        self._defense = self._level
        self._damage = self._level
        self._attackMove = [
                "Its teeth snap at you",
                "It tries to scartch you",
                "it circles around you and pounces"
            ]
class BugbearZombie(Enemy):
    def __init__(self, player):
        super().__init__(player)
        self._name = "Bugbear Zombie"
        self._description = "A Zombie of a Bugbear"
        self._health = self._level * 10
        self._attackChance = self._level
        self._defense = self._level
        self._damage = self._level
        self._attackMove = [
                "It swings at you with its axe",
                "It screams wiledly and slams into you",
                "It grabs you with a hand and wants to throw you at the wall"
            ]
class HumanZombie(Enemy):
    def __init__(self, player):
        super().__init__(player)
        self._name = "Human Zombie"
        self._description = "A Zombie of a Human"
        self._health = self._level
        self._attackChance = self._level
        self._defense = self._level
        self._damage = self._level
        self._attackMove = [
                "It bites you"
            ]
class Ghoul(Enemy):
    def __init__(self, player):
        super().__init__(player)
        self._name = "Ghoul"
        self._description = "A Ghoul of a Human"
        self._health = self._level * 5
        self._attackChance = self._level
        self._defense = self._level
        self._damage = self._level
        self._attackMove = [
                "It screams: 'I am HUUUUNGRY!!!!' and jumps at you",
                "With a finger it points to the right while trying to attack from the left",
                "It tries to shake your hand as a token of friendship. As soon as you try to grab it the Ghoul tries to bite of your hand",
                "It stares at you, you stare back. You feel a sharp pain inside you."
            ]
