T = [ -10, -8, 0, 1, 2, 5, -2, -4]
maior = T[0]
menor = T[0]
c = 0
s = 0
for x in T:
    if x > maior:
        maior = x
    if x < menor:
        menor = x
    c += 1
    s += x
print("!!Temperatura em Mons!!")
print(f"Máxima: {maior}\nMínima: {menor}")
print(f"Média: {s/c:.0f}")
