# the same last exercise, but now it accepts 2 rows.
# this one I decided to do completelly in english

last = 10
last2 = 10
row1 = list(range(1, last + 1))
row2 = list(range(1, last2 + 1))
x = 0
end = ""
while True:
    print(f"\nThere are {len(row1)} costumes in the first row\nand {len(row2)} in the second row.")
    operation = list(input("Operation to row 1 (A, F)\nOperation to row 2 (B, G)\n(S to exit both!):"))
    while x < len(operation):
        if operation[x] == "S":
            end = "S"
            break
        elif operation[x] == "A":
            if len(row1) > 0:
                served = row1.pop(0)
                print(f"ROW 1 - Costumer {served} was served")
            else:
                print("Empty row! Nobody to serv.")
        elif operation[x] == "F":
            last += 1
            row1.append(last)

        elif operation[x] == "B":
            if len(row2) > 0:
                served = row2.pop(0)
                print(f"ROW 2 - Costumer {served} was served")
            else:
                print("Empty row! Nobody to serv.")
        elif operation[x] == "G":
            last2 += 1
            row2.append(last2)
        else:
            print("Invalid oparation! type only A, B, F, G or S")
        x += 1
    if end == "S":
        break
    else:
        x = 0
