# program 6.6 rewritten to use 'for'
L = []
while True:
    n = int(input("Type a number (0 to exit):"))
    if n == 0:
        break
    L.append(n)

for x in L:
    print(x)

# only the second while was turned into for because the first while doesn't have a list to read,
# and the program need that looping estructure to add elements to the list constantily.
