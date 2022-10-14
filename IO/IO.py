# TODO
# public String giveItem(List<Room.Item> items, Room room) {
#         String returnString = "You have found a Chest containing following items:";
#         for (Room.Item item : items) {
#             if (item == Room.Item.gold || item == Room.Item.silver || item == Room.Item.bronze) {
#                 returnString += "\na " + item.toString() + " coin";
#             } else {
#                 returnString += "\na " + item.toString();
#             }          
#         }
#         returnString += "\n\nWhat do you want to pick up?";
#         System.out.println(returnString);
#         Scanner input = new Scanner(System.in);
#         System.out.print(">");
#         String answer = input.next();

#             if(answer.equals("everything")||answer.equals("all")){
#                 ListIterator<Room.Item> iterator = items.listIterator();
#                 int oldSize = items.size();
#                 returnString = "You have picked up the following items: ";
#                 while(iterator.hasNext()){
#                     Room.Item item = iterator.next();
#                     String itemString = recieveItem(item);
#                     if (itemString != ""){
#                         returnString += itemString +", ";
#                         if (itemWasGiven){
#                             iterator.remove();
#                         }
#                     }
#                 }
#                 if (items.size() == 0){
#                     returnString = "You have picked up all items";
#                 }
#                 else if (items.size() == oldSize){
#                     returnString = "You have not picked up any items. Please make room in your inventory using the drop command.";
#                 }
#             }                           
#             else if(answer.equals("nothing") || answer.length()<=0 || answer.equals("no")){
#                 return "You leave it all behind and turn around";
#             }
#             else{
#                 Boolean wrongItem = true;
#                 returnString = "You pick up a ";
#                 ListIterator<Room.Item> iterator = items.listIterator();
#                 int oldSize = items.size();
#                     while(iterator.hasNext()){
#                         Room.Item item = iterator.next();
#                         if (item.toString().equals(answer)){
#                             returnString += recieveItem(item);
#                             if (itemWasGiven){
#                                 iterator.remove();
#                             }
#                             wrongItem = false;
#                             break;
#                         }
#                     }
#                 if (wrongItem){
#                     returnString = "You can not pick up a " + answer + ". It seems to you that no matter how long you look in the box you will not find a "+answer;
#                 }
#                 else if (items.size() == oldSize){
#                     returnString = "You have not picked up any items. Please make room in your inventory using the drop command.";
#                 }
#             }    
#         return returnString;

import pyfiglet
print(pyfiglet.figlet_format("Mad Zork", font = "digital" ))

userInputs = [
    "go", "north", "soth", "east", "west", "back", "quit", "exit", "help", "inventory", "look", "take", "drop", "use", "open", "close", "talk", "attack", "fight", "run", 
    "search", "explore", "examine", "drink", "up", "down", "left", "right", "all", "everything", "nothing", "no", "yes", "y", "n"
]
def getUserInput():
    """
    Returns a String with the user input
    """
    userInput = input(">")
    return userInput
def validateUserInput(userInput):
    """
    Returns a boolean if a word in the user input is valid
    """
    userInput = userInput.lower()
    for word in userInput.split():
        if word in userInputs:
            return True
    return False