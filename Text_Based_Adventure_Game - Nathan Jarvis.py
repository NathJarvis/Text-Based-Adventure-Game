
"""
PLEASE READ BEFORE PROCEEDING!!!!

PLEASE OPEN WITH PYTHON SHELL TO ENSURE THE CLEAR FUNCTION WORKS, AS IT IS NOT SUPPORTED FOR IDE ENVIRONMENTS.
OR IF POSSIBLE CHANGE YOUR IDE TO SIMULATE TERMINAL OR SHELL WHEN THE CODE IS RUN.

"""

import os
import time

#storing user current area and user input as the choice variable
area = ""
choice = ""

#Creating user inventory, containing items from rooms that assist in the boss fight, the silver keys list and the gold key list.
#Also used for displaying in the hud.
#Mysical key list keeps the game running until the user has found the end key, once the key is appended to the list, the game ends.
mystical_key = []
silver_keys = []
gold_key = []
items = []
room_3_right_visited = False
room_3_middle_visited = False
room_3_middleback_visited = False

#Defining areas of the map and their connections, also stored dialogue for some rooms that do not have their own story section.
#The areas contain their own connections that are used later on to ensure a user can only go to rooms that are connected to the current room.
#Items are stored in the rooms and once collected, are deleted from the item dictionary so that they cannot be duplicated in the lists.
areas = {
    "Room 1" : {
        "Room":"Entrance",
        "Connections": {
            "Room 2":"Armoury",
            "Room 3":"Old Monster lair"
        },
        "Items": {},
        "Dialogue": "Welcome to the entrance of the dungeon.\n"
                    "Your mission is to find both silver keys to unlock room 5 and then the gold key.\n"
                    "The gold key will give you access to the boss room, where you must fight to gain the\n"
                    "dark matter mystical key, which will give you a lifetime full of money and power.\n"
    },
    "Room 2" : {
        "Room":"Armoury",
        "Connections": {
            "Room 1":"Entrance"
        },
        "Items": {
            "Item":"Armour"
        },
        "Dialogue": "Welcome to the armoury.\n"
                    "Although this room may seem like it leads to no where it may contain something that will help.\n"
                    "The Armoury was once used by a small group that were on an mission to eliminate the beast\n"
                    "that resides in this dungeon. If you think you have what it takes, grab some armour and finish what\n"
                    "the group couldn't....\n"
    },
    "Room 3" : {
        "Room":"Old Monster lair",
        "Connections": {
            "Room 4":"Bedroom",
            "Room 5":"Potion Room" #needs both Silver keys to unlock
        },
        "Items": {
            "Item1/2":"Silver Key 1",
            "Item":"Sword"
        },
        "Dialogue": ""
    },
    "Room 4" : {
        "Room":"Bedroom",
        "Connections": {
            "Room 3":"Old Monster lair",
            "Room 5":"Potion Room" #needs both Silver keys to unlock
        },
        "Items": {
            "Item":"Silver Key 2"
        },
        "Dialogue": "" #No dialogue as this room has its own story
    },
    "Room 5" : {
        "Room":"Potion Room",
        "Connections": {
            "Room 6":"Chest Room",
            "Room 7":"Boss Room"
        },
        "Items": {
            "Item":"Health Potion"
        },
        "Dialogue": "Welcome to the Potion Room.\n"
                    "When the beast retreated after the group attacked, they used this room as a checkpoint and stored health potions in here.\n"
                    "This was as far as they got and then they was never seen again. No one has ventured any further into room 6 or room 7.\n"
                    "There was reports of loud roars and noises from room 7. This is now believed to be where the beast resides. You do need a Key to get in there.\n"
                    "Rumour has it that the key is in room 6. However no one has ever been in there and successfully come out with the key....\n"
    },
    "Room 6" : {
        "Room":"Chest Room",
        "Connections": {
            "Room 5":"Potion Room"
        },
        "Items": {
            "Item":"Gold Key"
        },
        "Dialogue": "" #No dialogue as this room has its own story
    },
    "Room 7" : {
        "Room":"Boss Room",
        "Connections": {
        },
        "Items": {
            "Item":"Dark Matter Mystical Key",
        },
        "Dialogue": "" #No dialogue as this room has its own story
    }
}

#creating a function to clear the screen, created by importing the OS module which is part of the standard library.
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

#creating a function to display the directions for the user. The connections are stored in the area dictionary and are called up inside this function.
#Inside the function is also validation to ensure the user can only travel to rooms that are stored in the connections for the current room they are in.
def connections():
    print("Here are the rooms you can travel to:\n")
    for connection in areas[area]["Connections"]:
        print(connection + " - " + areas[area]["Connections"][connection])

#creating a function to check the room for items. It prints out all available items in the room and then appends it into the correct list. The item or key
#is then deleted from the item dictionary so that it cannot be duplicated in the lists.
def check_room():
    clear()
    hud()
    if areas[area]["Items"] == {}: #Some areas don't contain items, so this is to differentiate from if the item section is empty from picking up the item.
        print("There are no items in this room.\n")
        input("Press any key to continue.")
    elif areas[area]["Items"]["Item"] == "": #same as above, checks if the item is empty from picking up rather than it not existing.
        print("You have already picked these items up...\n")
        input("Press any key to continue.")
    else:
        print("You have found these items:")
        for Item in areas[area]["Items"]:
            print(areas[area]["Items"][Item])
        while True:
            print("\nWould you like to pick up these items?")
            choice = input("Answer (yes/no) > ")
            if choice.upper() == "YES":
                for Item in areas[area]["Items"]:
                    if areas[area]["Items"][Item] == "Silver Key 1" or areas[area]["Items"][Item] == "Silver Key 2":
                        silver_keys.append(areas[area]["Items"][Item])
                        areas[area]["Items"][Item] = ""
                    elif areas[area]["Items"][Item] == "Gold Key":
                        gold_key.append(areas[area]["Items"][Item])
                        areas[area]["Items"][Item] = ""
                    elif areas[area]["Items"][Item] == "Health Potion":
                        items.append(areas[area]["Items"][Item])
                        areas[area]["Items"][Item] = ""
                    elif areas[area]["Items"][Item] == "Sword":
                        items.append(areas[area]["Items"][Item])
                        areas[area]["Items"][Item] = ""
                    elif areas[area]["Items"][Item] == "Armour":
                        items.append(areas[area]["Items"][Item])
                        areas[area]["Items"][Item] = ""
                    elif areas[area]["Items"][Item] == "Dark Matter Mystical Key":
                        mystical_key.append(areas[area]["Items"][Item])
                        areas[area]["Items"][Item] = ""
                clear()
                hud()
                print("You have picked up the items, they are now in your inventory.\n")
                input("Press any key to continue.")
                break
            elif choice.upper() == "NO":
                clear()
                hud()
                print("You have chose to leave the items in the room.\n")
                input("Press any key to continue.")
                break
            else:
                clear()
                hud()
                print("Invalid input.\n")

#The HUD function is used to provide a constant display at the top of the screen. This provides information on the current room, Collected items
#Collected silver and gold keys.
def hud():
    clear()
    print("You are in the " + areas[area]["Room"])
    print(f"Items: {items}")
    print(f"silver_keys: {silver_keys}")
    print(f"gold_keys: {gold_key}")
    print("Press ctrl+c to quit the game at any time.\n")

#The check silver key function is used to check if the silver keys have been found and if so, allow the user to access Room 5.
#The user can only access Room 5 if both silver keys have been found, and one of these is collected by going through room 4
#containing the sleeping beast (Story section)
def check_silver_key():
    global area
    if silver_keys != ['Silver Key 1', 'Silver Key 2']:
        clear()
        hud()
        print("You have not found both silver keys yet. You are being redirected back to the connections selection\n")
        input("Press any key to continue.")
        while True:
            clear()
            hud()
            connections()
            print("\nWhich room would you like to go to?")
            print("E.g. Room 5, Room 1\n")
            choice = input("Answer > ")
            if choice.title() not in areas[area]["Connections"]:  # To ensure the user enters a valid room that is only a connection of the current room the user is in.
                print("\nInvalid input.")
            else:
                if area == "Room 4" and choice.title() == "Room 5":
                    print("You have already tried to go in this room but do not have the keys.")
                elif area == "Room 4" and choice.title() == "Room 3":
                    print("You are going back to the Old Monster Lair")
                    area = "Room 3"
                    input("Press any key to continue.")
                    break
                elif area == "Room 3" and choice.title() == "Room 5":
                    clear()
                    hud()
                    print("You have already tried to go in this room but do not have the keys.\n")
                    input("Press any key to go back to the connections selection.")
                elif area == "Room 3" and choice.title() == "Room 4":
                    area = "Room 4"
                    sleeping_beast()
                    break
                else:
                    print("Invalid input.\n")
                    input("Press any key to continue...\n")
    else:
        clear()
        hud()
        print("You use both silver keys to unlock the door to Room 5.\n")
        input("Press enter to continue...")
        area = "Room 5"

#The check gold key function is used to check if the gold key has been found and if so, allow the user to access Room 7, which is the boss room.
#The user can only access Room 7 if the gold key has been found in room 6 and added to the user inventory.
def check_gold_key():
    global area
    if gold_key == []:
        clear()
        hud()
        print("You have not found the gold key yet.\n")
        input("Press any key to continue.")
        area = "Room 5"
    else:
        clear()
        hud()
        print("You have found the gold key and can now access Room 7 (The boss room).\n")
        input("Press any key to continue.")
        area = "Room 7"
        boss_entrance()

#This is function 1 of 2 for the final boss fight, this function is called when the user enters Room 7 and provides an interactive way of
#either telling the user they have not found all the items and giving them the chance to go back or to let them continue but with a warning
#that they are at a disadvantage. The function then calls bossfight() which is the actual fight scene.
def boss_entrance():
    global area
    area = "Room 7"
    clear()
    hud()
    print("You Open the door with the gold key and see a long path surrounded by Lava on both sides.")
    print("You start to rethink whether you should continue....\n")
    input("Press any key to continue.")
    if items != ['Armour','Sword','Health Potion']:
        clear()
        hud()
        print("Listed below are the items you have not collected as you did not search these rooms. \nYou will still continue however, you will be at a disadvantage.\n")
        #Prints out what items the player is missing, it is impossible to miss the sword, so this is included in all the if statements.
        if items == ['Armour','Sword']:
            print("You have not found the Health Potion - This was located in Room 5.\n")
        elif items == ['Sword','Health Potion']:
            print("You have not found the Armor - This was located in Room 2.\n")
        elif items == ['Sword']:
            print("You have not found the Health Potion - This was located in Room 5.")
            print("You have not found the Armor - This was located in Room 2.\n")
        input("Press any key to continue.")
        boss_fight()
    else:
        clear()
        print("You have found all the items you need and decide to continue.")
        input("Press any key to continue.")
        clear()
        hud()
        print("You put your helmet, chest plate, boots, and chainmail on.")
        input("Press any key to continue.")
        clear()
        hud()
        print("You make sure you sword is readily available in its holster.")
        input("Press any key to continue.")
        clear()
        hud()
        print("You double check the health potion and make sure you know where it is.")
        input("Press any key to continue.")
        boss_fight()

#The main boss fight scene. This is the last scene and function of the game. It includes fight scenes where the boss hits certain rocks, and you have to hide behind them.
#If the boss hits your rock, you need to press keys to escape and flee the attack. Once you gain the confidence, you fight back and defeat the boss to gain access to the
#treasure and get your hands on the key, which ends the game.
def boss_fight():
    #Start of Scene 1
    clear()
    hud()
    print("You start to walk along the long dark purple brick path. Surrounded once again by lava on both sides.")
    print("At the end of the path you see a large platform with 3 tall stones and a chair facing backwards in the middle.")
    print("As you walk closer you hear a deep laugh and the chair slowly rotates round.")
    print("In front of you stands RazorBeast. 'You really thought you would come this far and make it out alive' He says.\n")
    input("Press any key to continue.")
    while True:
        clear()
        hud()
        print("Without a moment to think, RazorBeast throws a punch with his gigantic hand towards you.")
        print("You choose to hide behind a rock, but which one do you choose?\n")
        choice = input("Answer (1/2/3) > ")
        if choice == "1":
            clear()
            hud()
            print("RazorBeast hits Rock 2 but luckily you are safe.\n")
            input("Press any key to continue.")
            break
        elif choice == "2":
            clear()
            hud()
            print("Razorbeast hits the rock you hid behind, You leg gets pinnned with part of the broken rock!")
            print("Try to get it off!\n")
            input("Press any key to try and get it off!")
            input("It didnt work, try again!")
            clear()
            hud()
            print("You finally move the rock enough to run to another stone. Few!")
            input("Press any key to continue.")
            break
        elif choice == "3":
            clear()
            hud()
            print("RazorBeast hits Rock 2 but luckily you are safe.\n")
            input("Press any key to continue.")
            break
        else:
            clear()
            hud()
            print("Invalid input.\n")
            input("Press any key to continue.")
    # Start of Scene 2
    clear()
    hud()
    print("You gain the confidence to run toward RazorBeast and fight!")
    if items == ['Sword']:
        print("You run toward Razorbeast.")
        input("Press any key to swing your sword!")
        clear()
        hud()
        print("You land your sword on his arm and he lets out a gigantic roar.")
        print("You notice that arm is no longer moving, did you just get 1 step closer to defeating him?\n")
        input("Press any key to continue.")
    else:
        print("You run toward Razorbeast.")
        input("Press any key to kick a rock towards him!")
        clear()
        hud()
        print("You trip him up! He lands on one of his arm with a roar coming out of his mouth.")
        print("You notice that arm is no longer moving, did you just get 1 step closer to defeating him?\n")
        input("Press any key to continue.")
    while True:
        clear()
        hud()
        print("You notice him starting to charge up his swing again with his other arm.....")
        print("Without a moment to think, RazorBeast throws another punch with his other hand towards you.")
        print("You choose to hide behind a rock, but which one do you choose?\n")
        choice = input("Answer (1/2/3) > ")
        if choice == "1":
            clear()
            hud()
            print("Razorbeast hits the rock you hid behind!")
            if items == ['Sword']:
                print("Your sword is stuck under the rock. Try to get it out!")
                input("Press any key to try and get it out!")
                input("It didnt work, try again!")
                input("It doesnt budge, try any key to kick the rock as hard as you can")
                clear()
                hud()
                print("Finally, You pull your sword out and run to rock 3 (The only standing rock).")
                break
            else:
                clear()
                hud()
                print("You Just dodge the rock and run to the next stone. Few!")
                break
        elif choice == "2":
            clear()
            hud()
            print("This rock is already broken, try another one!")
        elif choice == "3":
            clear()
            hud()
            print("RazorBeast hits Rock 1 but luckily you are safe.")
            break
        else:
            clear()
            hud()
            print("Invalid input.\n")
            input("Press any key to continue.")
    print("With no more rocks left to hide behind you are face to face with RazorBeast, He grabs you at an instant and throws you down the path.")
    print("You manage to get back up but you are hurt....\n")
    input("Press any key to continue.")
    if 'Health Potion' in items:
        clear()
        hud()
        print("You remember you have your health potion in you inventory.")
        print("You drink it and the cuts and bruises all disappear. You feel much better.\n")
        input("Press any key to continue.")
        items.remove('Health Potion')
    else:
        clear()
        hud()
        print("You dont have a health potion in your inventory. You really wish you had one.")
        print("You rip a peice of your trouser to create a turneque to stop the bleeding from your wound.\n")
        input("Press any key to continue.")
    #Start of scene 3 (Final fight scene and gaining key from the chest)
    clear()
    hud()
    print("With all the built up anger you charge toward RazorBeast with 1 last final attempt at defeating him.")
    print("You leap in the air with height you never knew you could ever reach.\n")
    input("Press any key to continue.")
    if items == ['Sword']:
        clear()
        hud()
        input("Press any key to swing your sword.")
        clear()
        hud()
        print("You swing your sword towards him and hit him! He lets out a final gigantic roar.")
        print("RazorBeast drops to the ground and says 'This will not be the last you will see of me'.")
        print("You lay down in exhaustion, taking in everything that just happened....\n")
        input("Press any key to continue.")
    else:
        clear()
        hud()
        print("You kick him and he falls backwards, unable to gain his balance he falls into the lava, letting out one more final gigantic roar.")
        print("You lay down in exhaustion, taking in everything that just happened....\n")
        input("Press any key to continue.")
    clear()
    hud()
    print("After a few minutes you get back up")
    print("You head past RazorBeast toward the golden chest at the back of the platform.")
    print("You open it up and are showered with gold, diamonds and emeralds.\n")
    input("Press any key to continue.")
    clear()
    hud()
    print("Around all of the minerals you find a glowing dark purple key. It is the Dark Matter Mystical Key")
    print("You have found your key to the door out of the dungeon!\n")
    input("Press any key to pick up Dark Matter Mystical Key.")
    clear()
    hud()
    print("You have won the game!")
    print("Thanks for playing, I hope you enjoyed it!\n")
    print("The game will now end.")
    input("Press any key to exit the game.")
    exit()

#Room 4 includes a scene where the beast's pet is sleeping, in this room is a key which allows you to move onto room 5 (The potion room). There are 2 ways of approaching this scene.
#quiet means you get the key and can leave without waking the beast's pet. Quick means you wake the pet up, and it chases you out the room without the key. You then need to re-enter and
#try and get the key again.
def sleeping_beast():
    global area
    area = "Room 4"
    clear()
    hud()
    print("You enter the bedroom")
    print("You are not sure how to react when you spot a wild beast sleeping in the corner.")
    print("The room is dead silent and you try you hardest not to wake it up.\n")
    input("Press any key to continue.")
    if silver_keys != ['Silver Key 1','Silver Key 2']:
        while True:
            clear()
            hud()
            print("Would you like to search around the room or leave....\n")
            choice = input("Answer (search/leave) > ")
            if choice.upper() == "SEARCH":
                clear()
                hud()
                print("You head to the opposite side of the room and look through a pile of books on an old wooden desk.")
                print("You dont find anything interesting.")
                print("However, Out the corner of your eye you see something shining.")
                print("It looks like a silver key.....")
                print("You choose to go and get it. But do you go quietly or all out quick as possible?\n")
                choice = input("Answer (quick/quiet) > ")
                if choice.upper() == "QUICK":
                    clear()
                    hud()
                    print("You run toward the Key but kick a stone by accident at the beast.")
                    print("It wakes up and notices you are in the room. You both lock eyes and it growls as it starts to walk towards you.")
                    print("You choose to run away and come back when the beast has fallen asleep again to try and get the key.")
                    print("That was a close call.....\n")
                    input("Press any key to go back to safety.")
                elif choice.upper() == "QUIET":
                    clear()
                    hud()
                    print("You slowly creep to the opposite side of the room near where the beast is to try and take the key.")
                    print("The beast is within an arms length of you and you can feel its breath hitting the bottom of your leg.")
                    print("Without taking another step you reach out and grab the key.\n")
                    silver_keys.append("Silver Key 2")
                    print("Silently you unlock the door to room 5 and leave whilst the beasts pet is still sleeping\n")
                    input("Press any key to continue.")
                    area = "Room 5"
                    break
                else:
                    clear()
                    hud()
                    print("Invalid input.")
                    input("Press any key to continue.")
            elif choice.upper() == "LEAVE":
                clear()
                hud()
                print(f"You leave the room and head back to {areas["Room 3"]["Room"]}.")
                input("Press any key to continue.")
                room3_interactive()
                break
            else:
                clear()
                hud()
                print("Invalid input.")
                input("Press any key to continue.")
    else:
        while True:
            choice = input("Answer (search/leave) > ")
            if choice.upper() == "SEARCH":
                clear()
                hud()
                print("You remember searching this room before and finding a key.")
                print("This key may help you move to the next room.....")
                print("You are scared if you search anymore you may wake up the sleeping beast.\n")
                input("Press any key to continue.")
                clear()
                hud()
                print(f"You leave the room and head back to {areas["Room 3"]["Room"]}.")
                input("Press any key to continue.")
                area = "Room 3"
                break
            elif choice.upper() == "LEAVE":
                clear()
                hud()
                print(f"You leave the room and head back to {areas["Room 3"]["Room"]}.")
                input("Press any key to continue.")
                area = "Room 3"
                break
            else:
                print("Invalid input.")
                input("Press any key to continue.")

#First part of the room 6 (lava room) story. It allows the user the option to continue or leave the room before starting the story of the room.
#If the user chooses to continue, the room6_lava_story2 function is called up and the program continues. If they choose to leave, then the area is set
#back to Room 5, and the loop is broken to allow the travel back to Room 5.
def room6_lava_story1():
    global area
    area = "Room 6"
    clear()
    hud()
    print("You open the door of Room 6")
    print("To your surprise their is a thin stone brick line going straight ahead surrounded by lava. All the way at the end")
    print("you can see a metal chest. By now you are already sweating from the pure heat in the room.")
    print("You believe that in the chest is something that will unlock the door which leads to Room 7 - The Boss Room.\n")
    while True:
        clear()
        hud()
        print("Do you want to continue or leave and go back?\n")
        choice = input("Answer (Continue/leave) > ")
        if choice.upper() == "CONTINUE":
            room6_lava_story2()
            break
        elif choice.upper() == "LEAVE":
            clear()
            hud()
            print(f"You leave the room and head back to {areas["Room 5"]["Room"]}.")
            input("Press any key to continue.")
            area = "Room 5"
            break
        else:
            clear()
            hud()
            print("Invalid input.")
            input("Press any key to continue.")

#The second part of the room 6 (lava room) story. This part is the main story where the user has 2 different options on how to get past the lava to
#access the chest which contains the gold key for Room 7 (The boss room). This Lava story contains time.sleep() to break up the text as well as contains
#an input function that waits for user input to ensure the user is ready to continue.
def room6_lava_story2():
    global area
    area = "Room 6"
    clear()
    hud()
    print("You start to walk towards the single brick line leading to the chest.")
    print("Your heart starts to pound the closer you get. The heat of the lava from both sides intensifies.\n")
    input("Press any key to continue.")
    clear()
    hud()
    print("You take ur first steps onto the brick line")
    print("It does not feel sturdy at all, however you decide to continue. You notice up ahead a few bricks missing, What do you do?\n")
    while True:
        clear()
        hud()
        print("1. Try and jump over the gap (Highly would not recommend this....)")
        print("2. Use you sword to bridge the gap (May or may not work....)")
        choice = input("Answer (1/2) > ")
        if choice == "1":
            clear()
            hud()
            print("You went for the daredevil option and tried to jump over the gap.")
            input("Press any key to continue.")
            clear()
            hud()
            print("You leap and land on the brick on the other side. The brick slips and you fall to the side. You clench on with your finger tips.")
            print("You are now stuck dangling above the lava and feel like you are going to drop.")
            input("Press any key to continue.")
            clear()
            hud()
            print("You gain the strength and manage to climb back up to finish the brick line and reach the chest on the other side..")
            print("Inside the chest is a Gold Key. Could this possibly be the key to unlocking the door to the beast?")
            print("You also notice more brick lines lift out the lava to widen the once narrow path, clearing a safe route back to Room 5.")
            input("Press any key to continue.")
            clear()
            hud()
            print("You head back to Room 5 with the gold key in your inventory.\n")
            input("Press any key to continue.")
            if "Gold Key" not in gold_key:
                gold_key.append("Gold Key")
            area = "Room 5"
            break
        elif choice == "2":
            clear()
            hud()
            print("You chose to use your sword to bridge the gap (The safer option).")
            print("You place your sword between the gap, temporarily bridging between the two brick lines.")
            print("Although its sketchy and slippery, you decide to continue.\n")
            input("Press any key to continue.")
            clear()
            hud()
            print("You manage to cross the gap safely and reach the chest on the other side.")
            print("Inside the chest is a Gold Key. Could this possibly be the key to unlocking the door to the beast?")
            print("You also notice more brick lines lift out the lava to widen the once narrow path, clearing a safe route back to Room 5.\n")
            input("Press any key to continue.")
            clear()
            hud()
            print("You head back to Room 5 with the gold key in your inventory.\n")
            input("Press any key to continue.")
            if "Gold Key" not in gold_key:
                gold_key.append("Gold Key")
            area = "Room 5"
            break
        else:
            clear()
            hud()
            print("Invalid input.\n")
            input("Press any key to continue...\n")

#The interactive feature added to room 3 to break the game up a little and allow the player to be able to play more in depth in a specific room. The room
#has 3 areas that are able to be explored. Once these areas have been visited, you can no longer visit them to stop an infinite loop. It also ensures you pick up
#2 items before proceeding to room 5 (The potion room).
def room3_interactive():
    def room_3_right():
        def room_3_desk():
            while True:
                clear()
                hud()
                print("Which draw do you want to search?\n")
                print("1. Top Draw.")
                print("2. Middle Draw.")
                print("3. Middle Draw.\n")
                choice = input("Answer (1/2/3) > ")
                if choice == "1":
                    clear()
                    hud()
                    print("You search the top draw and find a ripped note with big letters on it.")
                    print("They seem to spell out; LAVA. Why would someone write down lava?\n")
                    input("Press any key to continue.")
                    break
                elif choice == "2":
                    clear()
                    hud()
                    print("You search the middle draw and find nothing interesting.")
                    print("You decide to search the top draw and find a ripped note with big letters on it.")
                    print("They seem to spell out; LAVA. Why would someone write down lava?\n")
                    input("Press any key to continue.")
                    break
                elif choice == "3":
                    clear()
                    hud()
                    print("You search the bottom draw and find nothing interesting.")
                    print("You decide to search the top draw and find a ripped note with big letters on it.")
                    print("They seem to spell out; LAVA. Why would someone write down lava?\n")
                    input("Press any key to continue.")
                    break
                else:
                    print("Invalid input.\n")
                    input("Press any key to continue.")

        while True:
            clear()
            hud()
            print("You go toward the wooden chair and desk.")
            print("Do you search the chair or desk first?\n")
            choice = input("Answer (Chair or Desk) > ")
            if choice.upper() == "CHAIR":
                clear()
                hud()
                print("You look underneath the chair and find nothing but broken wood and dust.")
                print("You then decide to move onto the desk and see if there is anything useful in it.\n")
                input("Press any key to continue.")
                room_3_desk()
                break
            elif choice.upper() == "DESK":
                room_3_desk()
                break
            else:
                clear()
                hud()
                print("Invalid input.")
                input("Press any key to try again...")

    def room_3_middle_back():
        clear()
        hud()
        print("You go toward the back of the room in the middle where there is a bed frame.")
        print("Its all rotten and nearly completely broken. You decide to look around it and see if there is anything useful.\n")
        input("Press any key to continue.")
        clear()
        hud()
        print("You notice etched into the side of the bed 'Fluffy', was this the beasts pet name?")
        print("You didnt expect the beast to use such friendly names...\n")
        input("Press any key to continue.")
        clear()
        hud()
        print("Next to the bed frame there is a leash, one that is not small enough for a normal dog...")
        print("It has thick metal spikes on it, what looks like to be blood remains, and a silver key dangling on it. This must have been for 'Fluffy'.")
        print("You start to think 'Fluffy' is not so Fluffy after all.")
        print("You decide to take the silver key off the leash\n")
        for Item in areas[area]["Items"]:
            if areas[area]["Items"][Item] == "Silver Key 1":
                silver_keys.append(areas[area]["Items"][Item])
                areas[area]["Items"][Item] = ""
            else:
                continue
        input("Press any key to continue.")

    def room_3_middle():
        global room_3_middle_visited
        clear()
        hud()
        print("You go towards the slightly lifted drain cover in the middle of the room.")
        print("You kick it but almost break your foot in the process from the weight of it.\n")
        input("Press any key to continue.")
        while True:
            clear()
            hud()
            print("Do you want to search around the drain cover or leave?\n")
            choice = input("Answer (search/leave) > ")
            if choice.upper() == "SEARCH":
                clear()
                hud()
                print("You notice scratched into the concrete a sentence.")
                print("Overtime its become more faint and is hard to read, but you manage to make a little bit out.")
                print("'Fluffy Water Bowl'. You start to wonder how Fluffy or the beast can even lift the lid in the first place.")
                print("You also say to yourself 'What animal drinks from a drain cover?'")
                print("Next to the drain cover there is a sword. You think this may be useful later in the dungeon so you take it.\n")
                input("Press any key to continue.")
                room_3_middle_visited = True
                for Item in areas[area]["Items"]:
                    if areas[area]["Items"][Item] == "Sword":
                        items.append(areas[area]["Items"][Item])
                        areas[area]["Items"][Item] = ""
                break
            elif choice.upper() == "LEAVE":
                break
            else:
                clear()
                hud()
                print("Invalid input.")
                input("Press any key to continue.")

    global area
    global room_3_middle_visited
    global room_3_right_visited
    global room_3_middleback_visited
    area = "Room 3"
    clear()
    hud()
    print("Welcome to the Old Monster Lair.\n")
    print("This room was where the beast once resided until the group tried attacking and pushed it\n"
    "further into the dungeon. Located in this room is something that will allow you to progress to another area.\n"
    "The item in this room was dropped when the group ran away from the beast as it grew stronger and fought back\n"
    "against them. You must be warned the beast had a pet that liked to sleep, its currently unknown where it is....\n")
    input("Press any key to continue.")
    while True:
        clear()
        hud()
        print("There are a few places you can search in this room.")
        print("1. Right - Old wooden chair with a rotting desk.")
        print("2. Middle Back - Old bed frame .")
        print("3. Middle - Slightly lifted drain cover.")
        print("4. Progress to room 4.\n")
        choice = input("Answer (1/2/3/4) > ")
        if choice == "1" and room_3_right_visited == False:
            room_3_right()
            room_3_right_visited = True
        elif choice == "1" and room_3_right_visited == True:
            clear()
            hud()
            print("You have already visited this section, Please select another option.\n")
            input("Press any key to continue.")
        elif choice == "2" and room_3_middleback_visited == False:
            room_3_middle_back()
            room_3_middleback_visited = True
        elif choice == "2" and room_3_middleback_visited == True:
            clear()
            hud()
            print("You have already visited this section, Please select another option.\n")
            input("Press any key to continue.")
        elif choice == "3" and room_3_middle_visited == False:
            room_3_middle()
        elif choice == "3" and room_3_middle_visited == True:
            clear()
            hud()
            print("You have already visited this section, Please select another option.\n")
            input("Press any key to continue.")
        elif choice == "4":
            if silver_keys == ['Silver Key 1'] and items == ['Sword'] or items == ['Sword', 'Armour'] or items == ['Armour', 'Sword']:
                sleeping_beast()
                break
            else:
                clear()
                hud()
                print("You have not picked up all the items to progress to the next room.")
                print("Please go back and pick up the items before continuing.\n")
                input("Press any key to continue.")
        else:
            clear()
            hud()
            print("Invalid input.")
            input("Press any key to continue.")

#The how to play provides information on the goals of the game and how to play the game. It also provides information on how to end
#the game at any time should the user want to.
def how_to_play():
    global area
    while True:
        global area
        clear()
        print("How to Play Guide")
        print("1. There are 7 rooms in the dungeon including the final boss room, each room contains items \n"
              "that will help you progress through the game and eventually aid in defeating the final boss.")
        print("2. Some doors are locked and require a key to open, some keys may be silver, some may be gold.....")
        print("3. The aim of the game is to collect all the items and unlock the final boss room to defeat the boss \n"
              "for the magical dark matter mystical key.")
        print("4. The game can be ended at any time by pressing ctrl+c.")
        print("5. Most important rule - Enjoy and have fun!\n")
        print("Would you like to continue or end the game? (continue/end) ")
        choice = input("Answer > ")
        if choice.upper() == "CONTINUE":
            area = "Room 1"
            break
        elif choice.upper() == "END":
            exit()
        else:
            clear()
            print("Invalid input.\n")
            input("Press any key to continue.")


#Start Game loop - The user can also access the how to play, which displays the instructions for the game.
clear()
while True:
    clear()
    print("Welcome to The Dungeon of RazorBeast")
    print("Have you played this game before?\n")
    choice = input("Answer (yes/no)> ")
    if choice.upper() == "YES":
        print("\nOkay, let's continue.\n")
        area = "Room 1"
        break
    elif choice.upper() == "NO":
        print("\nOkay, let's go through the How to Play guide.")
        how_to_play()
        break
    else:
        clear()
        print("Invalid input.")
        print("Try: Yes or No.\n")
        input("Press any key to continue.")


"""Main game Loop, This will run until the user quits the game by pressing ctrl+c.
The game runs off of a main loop and calls functions when required dependant on user input and rooms.
The rooms are stored in a dictionary called areas and contain items, keys, dialogue and also connections to other rooms. 
The user is given the option to travel to other rooms if they are stored within the current areas connections.
The user can also access the HUD at all times as this is displayed at the top of the screen with the user of a function and the clear function.
The HUD displays the current room, items, and keys as well as the details on how to exit the game."""
while mystical_key != ['Dark Matter Mystical Key']: #Keeps the game running so long as the user has not found the end key.
    while True:
        clear()
        hud()
        print(areas[area]["Dialogue"]) #Calls up room dialogue from the area dictionary if it is saturated.
        print("Do you want to search this room for Items and Keys?")
        choice = input("Answer (yes/no)> ")
        if choice.upper() == "YES":
            print()
            check_room()
            break
        elif choice.upper() == "NO":
            print("\nOkay.")
            break
        else:
            clear()
            hud()
            print(areas[area]["Dialogue"])  # Calls up room dialogue from the area dictionary if it is saturated.
            print("Invalid input.\n")
            input("Press any key to continue...\n")
    while True:
        clear()
        hud()
        print("Would you like to go to another room?\n")
        choice = input("Answer (yes/no)> ")
        if choice.upper() == "YES":
            clear()
            hud()
            connections()
            print("\nWhich room would you like to go to?")
            print("E.g. Room 5, Room 1")
            print("Type 'Back' to go back to the start of the room.")
            choice = input("\nAnswer > ")
            if choice.title() == "Back":
                break
            else:
                if choice.title() not in areas[area]["Connections"]: #To ensure the user enters a valid room that is only a connection of the current room the user is in.
                    print("Invalid input.")
                    input("Press any key to continue.")
                elif choice.title() != "Room 5" and choice.title() != "Room 7" and choice.title() != "Room 4" and choice.title() != "Room 6" and choice.title() != "Room 3":
                    area = choice.title()
                    break
                elif choice.title() == "Room 3":
                    room3_interactive()
                    break
                elif choice.title() == "Room 6":
                    room6_lava_story1()
                    break
                elif choice.title() == "Room 7":
                    check_gold_key()
                    break
                else:
                    clear()
                    hud()
                    print("Invalid input.\n")
                    input("Press any key to continue.")
        elif choice.upper() == "NO":
            clear()
            hud()
            print("You decide to stay in this room.\n")
            input("Press any key to continue.")
            break
        else:
            clear()
            hud()
            print("Invalid input.\n")
            input("Press any key to continue.")