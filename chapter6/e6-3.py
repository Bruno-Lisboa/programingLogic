# the exercise this time wanted to me to create a third list
# with the elements of first and second list, but without repeat
# the elements with the same values.
# one more fail to me yay \o/
list1 = []
list2 = []
list3 = []
spy = 0

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

while spy < len(list1):
   list3.append(list1[spy]) 
   spy += 1

print(f"list1 {list1} list3 {list3}")
