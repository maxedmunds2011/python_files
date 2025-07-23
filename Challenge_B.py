# Challenge B

username = input("What is your Minecraft username?") # Allows user to input their name as a string

wood_block_number = int(input("How many wood blocks do you currently have?")) # Allows user to input their wood block number as an integer
block_weight = float(input("How much does one block weigh (kg)?")) # Allows user to input the mass of the wood blocks as a float
daytime_choice = (input("Is it daytime in the game? Type True or False.")) # Allows user to store a person's preference as a string

if daytime_choice == "True": # When the user types True in the daytime choice question
    daytime_choice = True

else: # When the user types anything else in the daytime choice question
    daytime_choice = False

while wood_block_number < 10: # When the user has less than 10 wood blocks.
    print (f"You have {wood_block_number} blocks. You need {10 - wood_block_number} blocks.") # Subtract the number of wood blocks from 10
    wood_block_number = wood_block_number + int (input("How many blocks would you like to collect?")) # Add the wood block number string you enter to your previous number

print ("Collection Complete!") # Code for after the while statement breaks

# This section uses stored strings, integers and floats and regurgitates them
print (f"Player: {username}")
print (f"Total blocks: {wood_block_number}")
print (f"Total weight: {wood_block_number * block_weight} kg")
if daytime_choice == True: # Links to the boolean stored after typing "True"
    print("It is daytime.")
    
else: # If you had typed anything else back in the daytime choice question
    print("It's night. Watch out for mobs!")