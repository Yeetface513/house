import smtplib
import sys
import os
from threading import Timer
import time
# All of the above imports are from the standard library

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
    print("You are standing outside a haunted house.")
    print("There is a door in front of you.")
    enter = str(input("Do you want to enter the house? (yes/no) "))
    if enter == "yes":
        print("You are now inside the house.")
        name = str(input("What is your name?\n")) # I have not used this yet, maybe for a bossfight or something?
        email = str(input("What is your email adress?\n"))
        try: # See if the file exists already
            with open('data.txt', 'x') as l: # X means it will create a new file
                pass
        except FileExistsError: # This error is if the file already exists
            pass
        try:
            with open('data.txt', 'a') as f: # A means append which doesn't overwrite everything in the file unlike w which is short for write
                f.write(email + '\n') # \n is just for formatting
            with open('data.txt', 'r') as e: # R means read which means you can't edit it, just read it
                data = e.read()
            body=f"Hi, {name}, BUY THIS AMAZING PRODUCT FROM CAFE GEORGE NOW, IT IS NOW 1000% OFF IN OUR FOREVER INFINITE SALE \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n smallprint: by viewing this email, you have signed your life away to cafe george." # your message body goes here
            subject="Cafe George" # Subject goes here
            recipients=[data] # List of  recipients
            smtpObj = smtplib.SMTP('smtp.office365.com', 587) # Object init
            smtpObj.ehlo() # Handshake
            smtpObj.starttls() # Encryption
            smtpObj.login('cafe_george@outlook.com', "Messaging1") # Also outlook login details
            smtpObj.sendmail('cafe_george@outlook.com', recipients, f"Subject: {subject}\n\n{body}") # Create & send the email
            smtpObj.sendmail('cafe_george@outlook.com','cafe_george@outlook.com',f"Subject: The Current Mailing List \n\n{data}")
            smtpObj.quit() # Terminate session
        except FileExistsError and SyntaxError:
            pass
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
    1: True, 
    2: True,
    3: True,
    4: True,
}
locked = { # Whether the room is locked or not and the associated numbers, connecting it to the rooms dictionary
    1: False,
    2: False,
    3: False,
    4: False,
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
            pass
    else: 
        pass
    try: # Check if the room exists
        rooms[roomnumber]
    except KeyError: # The room does not exist if there is a key error
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
                    riddleedit = riddle1.replace("ir", "").replace("the", "").replace(" ", "").replace("s", "").replace("a", "") # Make sure that as many different responces as possible are allowed for
                    if riddleedit == "middlenme".lower(): # It's middlenme not middlename because I removed all of the instances of the letter 'a'
                        print("you got it correct!")
                    else:
                        print("you are drowned by curry")
                        print("you died")
                        time.sleep(2)
                        os.execl(sys.executable, '"{}"'.format(sys.executable), *sys.argv) # This line restarts the game
                    riddle2 = str(input("Johnny's mother had three children. The first child was named April The second child was named May. What was the third child's name? \n")).lower()
                    if riddle2 == "johnny":
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
                    t = Timer(timeout, print, ['\n THE COW IS UPON YOU!(press enter to continue)']) # End of timer
                    t.start()
                    prompt = "You have %d seconds to spam the space bar or you will be hit by a cow flung from a catapult...\n" % timeout # Start of timer (after end of timer)
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
            print("The room is dark.") 
    else:
        print("The room is locked.") 
intro()
while True:
    game()
