# nesse aqui eu ja tive que adicionar os centavos, e agora o variável valor recebe o input em float
# eu consegui medificar esse código e o anterior de primeira e ambos funcionaram corretamente de primeira também
# só que eu só que consegui fazer isso porque o código já estava bem estruturado e foi fácil identificar o padrão
# o problema é que eu continuo sem conseguir visualizar direito como esse porra funciona
# ainda tá difícil entender a lógica desse código
valor = float(input("Digite o valor a pagar: "))
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
        cédulas = 0
