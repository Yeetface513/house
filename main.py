import sys
import os
def intro():
     print("Welcome to haunted house, it is  very spooky scary skeleton!")
     print("You are standing outside a haunted house.")
     print("There is a door in front of you.")
     enter = str(input("Do you want to enter the house? (yes/no) "))
     if enter == "yes":
         print("You are now inside the house.")
         name = str(input("What is your name?\n"))
     else:
         print("Goodbye!")
         sys.exit()

rooms = {
    0: "door",
    1: "currydoor",
    2: "kitchen",
    3: "living room",
    4: "maccas",
    }
lit = {
    1: True,
    2: True,
    3: True,
    4: True,
}
locked = {
    1: False,
    2: False,
    3: False,
    4: False,
}
def game():
    roomnumber = int(input("What room do you want to go to? (1, 2, 3, 4 and 0 to leave) "))
    if roomnumber == 0:
        sure = str(input("Are you sure you want to leave? (yes/no) "))
        if sure == "yes":
            print("You have left the house.")
            sys.exit()
        else:
            pass
    else: 
        pass
    try:
        rooms[roomnumber]
    except KeyError:
        print("That room does not exist. The game is now restarting...." )
        os.execl(sys.executable, '"{}"'.format(sys.executable), *sys.argv)
        
    print(f"You are now in the {rooms[roomnumber]}")
    if lit[roomnumber] == True:
        print("The room is lit.")
    else:
        print("The room is dark.")
    if locked[roomnumber] == False:
        print("The room is not locked.")
    else:
        print("The room is locked.")
intro()
game()


