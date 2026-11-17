entry = input("anything: ")
d = {}
for s in entry:
    if s in d:
        d[s] = d[s] + 1
    else:
        d[s] = 1
print(d)

# Over 1 hour in this exercise and I didn't understand how to add key without a value to the dictionary

