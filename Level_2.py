print("Welcome to the game!")

print(42)
print(3.14)

name = "Bluey"
print(name)

name = "Bingo"
age = 6
print(name, "is", age, "years old.")

name = "Bluey"
age = 7
print(f"{name} is {age} years old.")  # ➜ Bluey is 7 years old.

print("Hello", end=" ")
print("world!")
# ➜ Hello world!

# String joining
greeting = "Hello" + " " + "World"
print(greeting)  # ➜ Hello World

# String repetition
laugh = "ha" * 3
print(laugh)  # ➜ hahaha


name = input("What is your name? ")
age = int(input("How old are you? "))     # Converts to integer
height = float(input("Your height in m? "))  # Converts to decimal (float)

if height > 1.8: # Height is above 1.8 metres
    print("Nice. You the Lebron!")

else: # Height is below 1.8 metres
    print("Bahaha you are an oompa loompa.")

if age < 12: # Height is below 12
    print("Go do something else with your life.") 

else:
    if age < 60: # Height is between 12 and 60
        print("Finally, a normal person.")

    else: # Height is 60 and higher
        print("Shouldn't you be dead?")
