# Practical 1
# making a simple output statement

print("Nirvana")
score = 100
lives = 5
myName ="Max"
print()
print(score)
print(lives)
print("Hello")
print("Welcome to the program")

# A program that prints out your name when using a Variable.
print(myName)
print()
print(f"My name is {myName}")

# Using if and else.
if score >= 50:
    print("You passed!")
else:
    print("Try again.")

# Using while.
while lives > 0:
    print("Keep playing")
    lives = -5
else:
    print("Too bad!")

# Using ranges for Variables and Numeric Code
for level in range(1, 4):
    print("Level", level)

# An assortment of variables.
name = "Alex"
score = 10
passed = True

# Code for greeting someone using a variable
def greet(name):
    print("Hello", name)

greet("John")

# Lets a user type something.
name = input("Max")
print()
print("Hi Max")

name = "Jan"
name = "Feb"
name = "Mar"
name = "Apr"
name = "May"
name = "Jun"
name = "Jul"
name = "Aug"
name = "Sep"
name = "Oct"
name = "Nov"
name = "Dec"

Jan = 23
Feb = 34
Mar = 33
Apr = 60
May = 12
Jun = 17
Jul = 28
Aug = 71
Sep = 70
Oct = 52
Nov = 48
Dec = 32

numbers = [Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec]
max_value = max(numbers)
print()
print(max_value)


# Practical 2