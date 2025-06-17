fruits = ["apple", "banana", "cherry"]
print(fruits)
# Lists use square brackets [ ] and each item is separated by a comma.


print(fruits[0])  # prints "apple"
print(fruits[2])  # prints "cherry"
# Use negative numbers to count from the end: fruits[-1] prints "cherry".


fruits[1] = "blueberry"
fruits.append("orange")
print(fruits)

 # Result: ['apple', 'blueberry', 'cherry', 'orange']


fruits.remove("apple")  # removes by name
del fruits[0]           # removes by position
print(fruits)
# Make sure the item exists before removing, or it will cause an error.


for fruit in fruits:
    print("I like", fruit)
# This is great for printing, checking, or using each item one by one.