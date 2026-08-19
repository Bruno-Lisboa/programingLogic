# esse programa verifica se um número é primo ou não.
número = int(input("Digite um número para verificar se ele é primo ou não: "))
if número % 2 == 0 and número != 2 or número == 1 or número == 0:
    print(f" {número} não é um número primo!")
elif número == 2:
    print(f" {número} é o único número primo que é par!")
else:
    impar = 3
    while impar <= número:
        if número == impar:
            print(f" {número} é um número primo!")
            break
        elif número % impar == 0 or número % 2 == 0:
            print(f" {número} não é um número primo!")
            break
        else:
            impar += 2
