print("what colour is the traffic light?")
lightColour = input()

print("what is the distance in meters to the intersection?")
distance = input()
distance = float(distance)

print("what is the speed of the car in meters")
speed = input()
speed = float(speed)

if lightColour == "green":
    print("Go")

if lightColour == "yellow":
    if speed <= 5:
        print("Go")
    else:
        print("Stop")

if lightColour == "red":
    if speed <= 2:
        print("Go")
    else:
        print("Stop")

if lightColour != "green" or "yellow" or "red":
    print("Stop") 

