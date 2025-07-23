while True:

    question = input("Please enter a number: ")
    print ("You entered", input)

    if question.isdigit():
        print("Valid.")
        break

    else:
        print("Invalid.")

print ("You have passed.")

# Example 2: Loop with break statement
# This loop will run until the condition is False or the break statement is encountered
num = 1
while True:
    print("Number:", num)
    num += 1
    
    if num >= 10:
        break

print("Finally broke out the loop")