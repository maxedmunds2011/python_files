name = input("What is your name?") # Stores user's name as string
age = int(input("How old are you?")) # Stores user's age as integer
snack = input("What snack would you like to bring?") # Stores user's snack choice as sring.
time_minutes = float(input("How long will the game last?")) # Stores user's gametime as float.
choice_waterplay = input("Do you like waterplay? (Type Yes/No without spaces)") # Stores user's waterplay choice as True/False

print ("Hi", name, "!") # Prints user's name
print (f"You're {age} years old and ready to play in Bluey's backyard.") # Prints user's age
print ("You'll play for", time_minutes, "minutes and bring your favourite snack:", snack +".") # Prints user's gametime and snack choice

if choice_waterplay == "Yes":
    waterplay = True # Stores user's waterplay choice as True

else:
    waterplay = False # Stores user's waterplay choice as False
    
if waterplay == True:
    
    print(f"Water play? {waterplay}! Better bring a towel!") # Prints user's waterplay choice (True)

else:
    print(f"Water play? {waterplay}! You don't need to do it to have fun!") # Prints user's waterplay choice (False)


games_list = ["Keepy Uppy", "Magic Asparagus", "Shadowlands", "Obstacle Course", "Muffin Cone"] # Sets up list 0 - 4
print(games_list) # Prints full list

print("First game:", games_list[0]) # Prints first game
print("Last game:", games_list[-1]) # Prints last game

games_list.append("Grannies") # Adds new variable to list
print(games_list) # Reprints list

games_list[1] = "Magic Wand" # Replaces Magic Asparagus with Magic Wand
print(games_list) # Reprints list

for game in games_list:
    print("Let's play:", game) # Prints each game with fun message

def count_games():
    print("Total games:", len(games_list)) # Counts how many games are on list

count_games()