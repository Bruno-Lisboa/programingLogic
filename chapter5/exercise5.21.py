# programa 5.1 reescrito com repetição aninhada
# esse código me persegue
# help
# demorei uns dois dias nesse exercício, mas consegui fazer. To muito feliz!
while True:
    valor = float(input("Digite o valor a pagar: "))
    apagar = valor
    cédulas = 0
    atual = 100
    if valor == 0:
        break
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
            elif atual == 1:
                atual = 0.50
            elif atual == 0.50:
                atual = 0.10
            elif atual == 0.10:
                atual = 0.05
            elif atual == 0.05:
                atual = 0.02
            elif atual == 0.02:
                atual = 0.01
            elif atual == 0.01:
                atual = 0.001
            cédulas = 0
