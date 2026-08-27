# the exercise this time wanted to me to create a third list     
# with the elements of first and second list, but without repeat the elements with the same values.
# this exercise was really important to me. It showed that I can learn programming, I just have to give the time to learn.
list1 = []
list2 = []

while True:
    addToList = int(input(f"add an element to the first list (0 when finished.): "))
    if addToList == 0:
        break
    else:
        list1.append(addToList)
while True:
    addToList = int(input(f"add an element to the second list (0 when finished.): "))
    if addToList == 0:
        break
    else:
        list2.append(addToList)

list3 = list1[:] + list2[:]
finalList = []
if len(list3) == 0:
    print("You didn't add any element to the lists!")
else:
    finalList.append(list3[0])
add = 0
check = 0

while add < len(list3) and check < len(finalList):
    if list3[add] == finalList[check]:
        add += 1
        check = 0
    elif check == len(finalList) - 1:
        finalList.append(list3[add])
    else:
        check += 1

print(finalList)
