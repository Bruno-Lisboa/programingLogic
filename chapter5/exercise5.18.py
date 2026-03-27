# se você é doido e ta lendo isso, eu modifiquei o programa do exercício 5.16 pra aceitar nota R$100
# é só isso mesmo
# puta que pariu. eu faço o programa funcionar e ainda assim ta confuso pra mim nesse momento.
valor = int(input("Digite o valor a pagar: "))
cédulas = 0
atual = 100
apagar = valor
while True:
    if atual <= apagar:
        apagar -= atual
        cédulas += 1
    else:
        print(f"{cédulas} cédulas(s) de R${atual}")
        if apagar == 0:
            break
        if atual == 100:
            atual = 50
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        cédulas = 0
