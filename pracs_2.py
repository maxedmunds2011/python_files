name = input("What is your name? ")

# Starting values
health = 100
food = 50
in_cave = True

hours = int(input("How many hours did you wait in the cave? "))

# Algorithm - apply effects
health -= hours * 5
food -= hours * 3

# Show result
print(f"\n{name}, your health is now {health}")
print(f"Your food is now {food}")

# Condition check
if health < 50 or food < 20:
    print("Warning: You are weak!")

if health < 0 or food < 0:
    print("You died!")

if hours >= 5 and health > 0 and food > 0:
    print("You survived the cave night!")
else:
     if hours < 5 and health > 0 and food > 0:
      print("You left too early and got attacked!")
      print("Bye Bye!!!")

     else:
         print("Bye Bye!!!")
