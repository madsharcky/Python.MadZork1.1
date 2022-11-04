import pyfiglet
print(pyfiglet.figlet_format("Mad Zork", font = "digital" ))

__ValiduserInputs = [
    "go", "back", "north", "soth", "east", "west", "up", "down", "left", "right",
    "quit", "help", "inventory", "map", 
    "look", "explore", "examine", "search",
    "drop", "take", "use", "drink", "open",  
    "all", "everything", "nothing", "no", "yes", "y", "n", "do", "don't", 
    "kick", "stab", "hit", "attack", "fight", "punch", "kill", "run", "retreat", "flee"
    ]
def getValidUserInputs():
    """
    Returns a list of all valid user inputs
    """
    return __ValiduserInputs

def __validateUserInput(userInput):
    """
    Returns a boolean if a word in the user input is valid
    """
    for word in userInput.lower().split():
        if word in __ValiduserInputs:
            return True
    return False
def __getCommands(userInput):
    """
    Returns a List with the commands, getting rid of all the filler words
    """
    command = []
    for word in userInput.lower().split():
        if word in __ValiduserInputs:
            command.append(word)
    return command

def getCommandFromUserInput():
    """
    Prompts the User to make an Input and returns a list of comands if the input is valid
    """
    userInput = input(">")
    while not __validateUserInput(userInput):
        print("I don't understand that")
        userInput = input(">")
    return __getCommands(userInput)
