#Program that calculate travelled time
distance = int(input("Tell me the distance in kilometers: "))
carSpeed = int(input("Now, in kilometers, put the speed you are going: "))
time = distance/carSpeed
timeInMinutes = int(time * 60)
print(f"You will spend {time:.1f}h traveling")
print(f"This is {timeInMinutes}min")
