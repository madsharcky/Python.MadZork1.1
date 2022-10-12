class Game:
    def __init__(self):
        self.name = "MadZork"
        self.version = "0.1"
        self.author = "Mad Sharcky"
        self.description = "MadZork is a text adventure game."
        self.license = "MIT"
        self.finished = False
        self.playerClass = ""
        self.attackCount = 0
        self.finished = False
        self.retreat = False
        self.alcoholSips = 0
        self.currentEnemy = None

        self.printWelcome()
        while self.playerClass == "":
            self.selectClass()

    def selectClass(self):        
        print("")
        print("Select a class:")
        print("1. Warrior")
        print("2. Mage")
        print("3. Thief")
        playerClass = input("> ")
        match (playerClass):
            case "1" | "Warrior" | "warrior":
                print("You are a Warrior!")
                self.playerClass = "Warrior"
            case "2" | "Mage" | "mage":
                print("You are a Mage!")
                self.playerClass = "Mage"
            case "3" | "Thief" | "thief":
                print("You are a Thief!")
                self.playerClass = "Thief"
            case _:
                print("Invalid class.")     
                self.playerClass = ""               


    def printWelcome(self):
        print("Welcome to " + self.name + "!")
        print(self.description)
        print("Version: " + self.version)
        print("Author: " + self.author)
        print("License: " + self.license)
        print("Press any key to continue...")
        input()


    def play(self):
        while (not self.finished):
            print("You are in a room.")
            print("What do you do?")
            command = input("> ")
            if (command == "quit"):
                self.finished = True
        print("Thanks for playing!")