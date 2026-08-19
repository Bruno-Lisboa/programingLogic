# alterando o código anterior parar mostrar os x primeiros números primos
# não consegui fazer esse :(
# não vou nem tentar fazer certo, deixo aqui registrado minha falha
número = int(input("Digite um número para verificar se ele é primo ou não: "))
if número < 0:
    print(" ERROR: Apenas números positivos são aceitos!")
elif número % 2 == 0 and número != 2 or número == 1 or número == 0:
    print(f" {número} não é um número primo!")
elif número == 2:
    print(f" {número} é o único número primo que é par!")
else:
    impar = 3
    while impar <= número:
        if número == impar:
            print(f" {número} é um número primo!")
            break
        elif número % impar == 0:
            print(f" {número} não é um número primo!")
            break
        else:
            impar += 2
# esse código ta aqui em baixo porque eu tava testando se ia dar certo
# depois eu colocar no lugar apropriado
    count = 0
    impar2 = 3
    n2 = 5
    repeat = int(input("repetição: "))
    while impar2 < n2:
        if count == repeat:
            break
        else:
            if n2 % impar2 == 0:
                impar2 += 4
            print(impar2)
            impar2 += 2
            n2 += 2
        count += 1
