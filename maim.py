# THIS CODE RELIES ON A TEXT FILE CALLED DATA.TXT
import smtplib # import module (is a builtin)
import sys # This is from the standard library
import os # This is from the standard library
from threading import Timer # This is from the standard library
import time # This is from the standard library
import json # This is from the standard library

print("annoying test!")

def intro():
    print("""
 █     █░▓█████  ██▓     ▄████▄   ▒█████   ███▄ ▄███▓▓█████    ▄▄▄█████▓ ▒█████     ▄▄▄█████▓ ██░ ██ ▓█████     ██░ ██  ▒█████   █    ██   ██████ ▓█████  ▐██▌  ▐██▌  ▐██▌ 
▓█░ █ ░█░▓█   ▀ ▓██▒    ▒██▀ ▀█  ▒██▒  ██▒▓██▒▀█▀ ██▒▓█   ▀    ▓  ██▒ ▓▒▒██▒  ██▒   ▓  ██▒ ▓▒▓██░ ██▒▓█   ▀    ▓██░ ██▒▒██▒  ██▒ ██  ▓██▒▒██    ▒ ▓█   ▀  ▐██▌  ▐██▌  ▐██▌ 
▒█░ █ ░█ ▒███   ▒██░    ▒▓█    ▄ ▒██░  ██▒▓██    ▓██░▒███      ▒ ▓██░ ▒░▒██░  ██▒   ▒ ▓██░ ▒░▒██▀▀██░▒███      ▒██▀▀██░▒██░  ██▒▓██  ▒██░░ ▓██▄   ▒███    ▐██▌  ▐██▌  ▐██▌ 
░█░ █ ░█ ▒▓█  ▄ ▒██░    ▒▓▓▄ ▄██▒▒██   ██░▒██    ▒██ ▒▓█  ▄    ░ ▓██▓ ░ ▒██   ██░   ░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄    ░▓█ ░██ ▒██   ██░▓▓█  ░██░  ▒   ██▒▒▓█  ▄  ▓██▒  ▓██▒  ▓██▒ 
░░██▒██▓ ░▒████▒░██████▒▒ ▓███▀ ░░ ████▓▒░▒██▒   ░██▒░▒████▒     ▒██▒ ░ ░ ████▓▒░     ▒██▒ ░ ░▓█▒░██▓░▒████▒   ░▓█▒░██▓░ ████▓▒░▒▒█████▓ ▒██████▒▒░▒████▒ ▒▄▄   ▒▄▄   ▒▄▄  
░ ▓░▒ ▒  ░░ ▒░ ░░ ▒░▓  ░░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░   ░  ░░░ ▒░ ░     ▒ ░░   ░ ▒░▒░▒░      ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░    ▒ ░░▒░▒░ ▒░▒░▒░ ░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░░░ ▒░ ░ ░▀▀▒  ░▀▀▒  ░▀▀▒ 
  ▒ ░ ░   ░ ░  ░░ ░ ▒  ░  ░  ▒     ░ ▒ ▒░ ░  ░      ░ ░ ░  ░       ░      ░ ▒ ▒░        ░     ▒ ░▒░ ░ ░ ░  ░    ▒ ░▒░ ░  ░ ▒ ▒░ ░░▒░ ░ ░ ░ ░▒  ░ ░ ░ ░  ░ ░  ░  ░  ░  ░  ░ 
  ░   ░     ░     ░ ░   ░        ░ ░ ░ ▒  ░      ░      ░        ░      ░ ░ ░ ▒       ░       ░  ░░ ░   ░       ░  ░░ ░░ ░ ░ ▒   ░░░ ░ ░ ░  ░  ░     ░       ░     ░     ░ 
    ░       ░  ░    ░  ░░ ░          ░ ░         ░      ░  ░                ░ ░               ░  ░  ░   ░  ░    ░  ░  ░    ░ ░     ░           ░     ░  ░ ░     ░     ░    
                        ░                                                                                                                                                  
    """) # Ascii art introduction
    print("You are standing outside a haunted house.") # Introduction
    print("There is a door in front of you.") # Introduction
    enter = str(input("Do you want to enter the house? (yes/no) "))
    if enter == "yes":
        print("You are now inside the house.")
        name = str(input("What is your name?\n")) # I have not used this yet, maybe for a bossfight or something?
        email = str(input("What is your email adress?\n"))
        with open('data.txt', 'a') as f:
            f.write(email + '\n')
        with open('data.txt', 'r') as e:
            data = e.read()
        body=f"Hi, {name}, BUY THIS AMAZING PRODUCT FROM CAFE GEORGE NOW, IT IS NOW 1000% OFF IN OUR FOREVER INFINITE SALE \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n smallprint: by viewing this email, you have signed your life away to cafe george." # your message body goes here
        subject="Cafe George" # your subject goes here
        recipients=[data] # list of your recipients
        smtpObj = smtplib.SMTP('smtp.office365.com', 587) # object init
        smtpObj.ehlo() # handshake
        smtpObj.starttls() # encryption
        smtpObj.login('cafe_george@outlook.com', "Messaging1") # also outlook login details
        smtpObj.sendmail('cafe_george@outlook.com', recipients, f"Subject: {subject}\n\n{body}") # create & send the email
        smtpObj.sendmail('cafe_george@outlook.com','cafe_george@outlook.com',f"Subject: The Current Mailing List \n\n{data}")
        smtpObj.quit() # terminate session
    else:
        print("Goodbye!")
        sys.exit()

boss = "Aahan Pathak"

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
        f = open("amongus.txt", "a")
        f.write("Now the file has more content!")
        f.close()
        os.execl(sys.executable, '"{}"'.format(sys.executable), *sys.argv) # This line restarts the game
        
    print(f"You are now in the {rooms[roomnumber]}") # This line tells the user what room they are in
    if locked[roomnumber] == False:
        print("The room is not locked.") # More lock functionality planned
        if lit[roomnumber] == True:
            print("The room is lit.") # More light functionality planned
            try: # Check if the item exists
                if roomnumber ==1:
                    print("the room is overflowing with curry \n there are a set of riddles you must complete.")
                    riddle1 = str(input("What do Alexander The Great and Winnie The Pooh have in common? \n"))
                    if riddle1 == "middle name".lower() or "a middle name".lower() or "their middle names".lower() or "middle names".lower():
                        print("you got it correct!")
                    else:
                        print("you are drowned by curry")
                        print("you died")
                        time.sleep(2)
                        os.execl(sys.executable, '"{}"'.format(sys.executable), *sys.argv) # This line restarts the game
                    riddle2 = str(input("Johnny's mother had three children. The first child was named April The second child was named May. What was the third child's name? \n"))
                    if riddle2 == "johnny".lower():
                        print("you got it correct!")
                    else:
                        print("you are drowned by curry")
                        print("you died")
                        time.sleep(2)
                        os.execl(sys.executable, '"{}"'.format(sys.executable), *sys.argv) # This line restarts the game
                    print("you have escaped the curry door!")
                if roomnumber == 2:
                    timeout = 2
                    print("I fart in your general direction! \n your mother was a hamster and your father smelt of elderberries! \n Fetchez La Vache!")
                    time.sleep(1)
                    t = Timer(timeout, print, ['\n THE COW IS UPON YOU!(press enter to continue)'])
                    t.start()
                    prompt = "You have %d seconds to spam the space bar or you will be hit by a cow flung from a catapult...\n" % timeout
                    answer = input(prompt)
                    t.cancel()
                    spaceAmount = answer.count(' ')
                    if spaceAmount >=10:
                        print("you have dodged the cow!")
                    else:
                        print("the cow has squashed you...")
                        print("you died")
                        time.sleep(2)
                        os.execl(sys.executable, '"{}"'.format(sys.executable), *sys.argv) # This line restarts the game
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
while True:
    game()
