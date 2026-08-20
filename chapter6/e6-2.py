list1 = []
list2 = []
while True:
    elist1 = int(input(f"add an element to the first list (0 when you're done.): "))
    if elist1 == 0:
        break
    list1.append(elist1)

while True:
    elist2 = int(input(f"add an element to the second list (0 when you're done.): "))
    if elist2 == 0:
        break
    list2.append(elist2)

list3 = list1[:] + list2[:]
print(f"These are all the elements chosen {list3}")
