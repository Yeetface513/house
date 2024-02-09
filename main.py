import sys # This is from the standard library
import os # This is from the standard library
def intro():
     print("Welcome to haunted house, it is  very spooky scary skeleton!") # Introduction
     print("You are standing outside a haunted house.") # Introduction
     print("There is a door in front of you.") # Introduction
     enter = str(input("Do you want to enter the house? (yes/no) "))
     if enter == "yes":
         print("You are now inside the house.")
         name = str(input("What is your name?\n")) # I have not used this yet, maybe for a bossfight or something?
     else:
         print("Goodbye!")
         sys.exit()

rooms = { # The names of the rooms and their associated numbers
    0: "door",
    1: "currydoor",
    2: "kitchen",
    3: "living room",
    4: "maccas",
    }
lit = { # Whether the room is lit or not and the associated numbers, connecting it to the rooms dictionary
    1: True, # Bool 
    2: True, # Bool
    3: True, # Bool
    4: True, # Bool
}
locked = { # Whether the room is locked or not and the associated numbers, connecting it to the rooms dictionary
    1: False, # Bool
    2: False, # Bool
    3: False, # Bool
    4: False, # Bool
}
items = {
    1: "key",
    2: "holy grail",
    3: "fork",
    4: "spoon",
}
invitems = {

}
def game():
    roomnumber = int(input("What room do you want to go to? (1, 2, 3, 4 and 0 to leave) "))
    if roomnumber == 0:
        sure = str(input("Are you sure you want to leave? (yes/no) "))
        if sure == "yes":
            print("You have left the house.")
            sys.exit()
        else:
            pass # Does nothing
    else: 
        pass # Does nothing
    try: # Check if the room exists
        rooms[roomnumber]
    except KeyError:
        print("That room does not exist. The game is now restarting...." )
        os.execl(sys.executable, '"{}"'.format(sys.executable), *sys.argv) # This line restarts the game
        
    print(f"You are now in the {rooms[roomnumber]}") # This line tells the user what room they are in
    if locked[roomnumber] == False:
        print("The room is not locked.") # More lock functionality planned
        if lit[roomnumber] == True:
            print("The room is lit.") # More light functionality planned
            try: # Check if the item exists
                print(f"You can see a {items[roomnumber]} in the room.") # This line tells the user what item is in the room
                if len(invitems)<3:
                    pickup = str(input("Do you want to pick it up? (yes/no) \n"))
                    if pickup == "yes":
                        print(f"You have picked up the {items[roomnumber]}.")
                        invitems[roomnumber] = items.pop(roomnumber)
                        invitems[len(invitems)] = invitems[roomnumber]
                        del invitems[roomnumber]
                else:
                    drop = str(input("You have too many items, do you want to get rid of some? (yes/no)"))
                    if drop == "yes":
                        droppeditem = int(input("Which numbered item from your inventory in order of which you got them would you like to remove? (1,2,3 etc)"))
                        del invitems[droppeditem]
                    else:
                        pass
            except KeyError:
                print("There is nothing in the room.")
        else:
            print("The room is dark.") # More light functionality planned
    else:
        print("The room is locked.") # More lock functionality planned
intro()
game()
