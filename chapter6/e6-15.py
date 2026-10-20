# modify the program 6.13 to ask the available rooms and sits in the cinema
sits = []
room = int(input("How many available rooms in the cinema today? "))
while True:
    if room == 0 or room < 0:
        print("Session finished!")
        break
    else:
        while room != 0:
            sits.append(0) 
            room -= 1
    for r, e in enumerate(sits):
        sits[r] = int(input(f"Room {r + 1} - how many available sits? "))

for r, e in enumerate(sits):
    print(f"Room {r + 1} | {e} Sits available")

