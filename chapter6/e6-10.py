L = [15, 7, 27, 39]
p = int(input("Digite o primeiro valor a procurar:"))
v = int(input("Digite o segundo valor a procurar:"))
x = 0
while x < len(L):
    if L[x] == p:
        print(f"{p} foi encontrado na posição {x}")
    if L[x] == v:
        print(f"{v} foi encontrado na posição {x}")
    x += 1
