ground = 0
maxHeight = 100
rocketLocation = 0
speed = 5



while rocketLocation <= maxHeight:
    print ("Rocket location is ", rocketLocation, "!")
    rocketLocation += speed
    import time
    print("Start")
    time.sleep(1)
    print("Waited 1 second")

print ("Max height has been reached!")

while rocketLocation >= ground:
    print ("Rocket location is ", rocketLocation, "!")
    rocketLocation -= speed
    import time
    print("Start")
    time.sleep(1)
    print("Waited 1 second")

print ("Rocket has landed.")