name = input("What is your name?")
age = int(input("How old are you?"))
snack = input("What snack would you like to bring?")
time_minutes = float(input("How long will the game last?"))
choice_waterplay = input("Do you like waterplay? (Type Yes/No without spaces)")

print ("Hi", name, "!")
print ("You're", age, "years old and ready to play in Bluey's backyard.")
print ("You'll play for", time_minutes, "minutes and bring your favourite snack:", snack +".")

if choice_waterplay == "Yes":
    waterplay = True

else:
    waterplay = False
    
if waterplay == True:
    
    print("Water play?", waterplay, "! Better bring a towel!")

else:
    print("Water play?", waterplay, "! You don't need to do it to have fun!")


games_list = ["Keepy Uppy", "Magic Asparagus", "Shadowlands", "Obstacle Course", "Muffin Cone"]
print(games_list)
print("First game:", games_list[0])
print("Last game:", games_list[-1])