L = [15, 7, 27, 39]
p = int(input("Digite o primeiro valor a procurar:"))
v = int(input("Digite o segundo valor a procurar:"))
x = 0
pp = 5
vv = 5
while x < len(L):
    if L[x] == p:
        pp = x
    if L[x] == v:
        vv = x
    x += 1

if pp < vv:
    print(f"{p} Foi achado primeiro!")
if vv < pp:
    print(f"{v} Foi achado primeiro!")

if pp == 5:
    print(f"{p} Não foi encontrado!")
if vv == 5:
    print(f"{v} Não foi encontrado!")
