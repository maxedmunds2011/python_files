# functions.py
import os

from colorama import init, Fore, Style
init(autoreset=True)

def show_location(room_name, rooms):
    room = rooms[room_name]
    print(Style.BRIGHT + Fore.YELLOW + f"\nYou are in {room_name.upper()}")
    print(room["description"])
    if room["items"]:
        print(Fore.CYAN + "You see:", ", ".join(room["items"]))
    print(Fore.GREEN + "Exits:", ", ".join(room["exits"].keys()))

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_location(room_name, rooms):
    room = rooms[room_name]
    print("\nYou are in", room_name.upper())
    print(room["description"])
    if room["items"]:
        print("You see:", ", ".join(room["items"]))
    print("Exits:", ", ".join(room["exits"].keys()))

def get_command():
    return input("\nWhat do you do? ").strip().lower()

def move(current_room, direction, rooms):
    if direction in rooms[current_room]["exits"]:
        return rooms[current_room]["exits"][direction]
    else:
        print("You can't go that way.")
        return current_room

def take_item(room_name, item, rooms, inventory):
    room = rooms[room_name]
    if item in room["items"]:
        inventory.append(item)
        room["items"].remove(item)
        print(f"You took the {item}.")
    else:
        print(f"There is no {item} here.")

def check_end_game(current_room, inventory):
    if current_room == "escape_pod":
        if "keycard" in inventory:
            print("You insert the keycard. The pod launches. You’ve escaped!")
            print("ENDING: FREEDOM")
            return True
        else:
            print("You need a keycard to launch the escape pod.")
    if current_room == "hallway" and "blaster" in inventory:
        print("You’re spotted by a patrol droid. You fire!")
        print("ENDING: GUNFIGHT IN THE HALLWAY")
        return True
    return False

print(Fore.YELLOW + "You are in the ARMOURY.")
print(Fore.CYAN + "You see: blaster")
print(Fore.RED + "You can't go that way.")