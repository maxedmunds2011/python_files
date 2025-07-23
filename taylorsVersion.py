# correct this code
swiftAlbums=["Taylor Swift","Fearless","Speak Now","Red","1989","Reputation","Lover"]

print("Taylor Swift Albums:")
for album in swiftAlbums:
    print(album)

albumToCheck = input("Enter an album to check: ")
if albumToCheck in swiftAlbums:
    print(f"{albumToCheck} is in the list")
else:
    print(f"{albumToCheck} is not in the list")

# The while loop version
counter = 0
max_counter = 3

while counter < max_counter:
    
    albumToCheck = input("Enter an album to check or type 'exit' to quit: ")

    if albumToCheck == "exit":
        break

    if albumToCheck in swiftAlbums:
        print(f"{albumToCheck} is in the list")
    else:
        print(f"{albumToCheck} is not in the list")

    counter += 1

    if counter == max_counter:
        break



print("You've exceeded your maximum tries. Thank you.")
