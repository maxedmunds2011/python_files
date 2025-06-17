trains = [['Nozomi', 300], ["Mizuho", 310], ["Sakura", 220], ["Hikari", 250], ["Kodama", 200], ["Tsumabe", 225]]

# Access speeds of all trains
train_average = (trains[0][1] + trains[1][1] + trains[2][1] + trains[3][1] + trains[4][1] + trains[5][1]) / 6
print("Train average is " + str (train_average))  # Output: 250.83
