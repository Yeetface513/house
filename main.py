import sys
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
def game():
    roomnumber = int(input("What room do you want to go to? (1, 2, 3, 4 and 0 to leave) "))
    if roomnumber == 0:
        sure = str(input("Are you sure you want to leave? (yes/no) "))
        if sure == "yes":
            print("You have left the house.")
            sys.exit()
        else:
            pass
    print(f"you are now in the {rooms[roomnumber]}")
intro()
game()


