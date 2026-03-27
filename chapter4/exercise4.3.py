#Write a program that asks for 3 numbers and print the major and minor
N1 = int(input("Número 1: "))
N2 = int(input("Número 2: "))
N3 = int(input("Número 3: "))

if N1 == N2 and N1 == N3:
    print(f"{N1} foi o único número digitado!")

if N1 > N2 and N1 > N3 or N1 > N2 and N1 == N3 or N1 > N3 and N1 == N2:
    print(f"{N1} é o maior número!")
if N2 > N1 and N2 > N3 or N2 > N1 and N2 == N3:
    print(f"{N2} é o maior número!")
if N3 > N1 and N3 > N2:
    print(f"{N3} é o maior número!")

if N1 < N2 and N1 < N3 or N1 < N2 and N1 == N3 or N1 < N3 and N1 == N2:
    print(f"{N1} é o menor número!")
if N2 < N1 and N2 < N3 or N2 < N1 and N2 == N3:
    print(f"{N2} é o menor número!")
if N3 < N1 and N3 < N2:
    print(f"{N3} é o menor número!")
