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
    "door": 0,
    "currydoor": 1,
    "kitchen": 2,
    "Livingroom": 3,
    "maccas": 4,
    }
intro()
def game():
    roomnumber = int(input("What room do you want to go to? (1, 2, 3, 4 and 0 to leave) "))
    if roomnumber = 0:
        print("You have left the house.")
        sys.exit()
    else:
        print()


