# program 6.13 modified to print the total of tickets sold
lv = [10, 2, 1, 3, 0] # lv = lugares vagos
ingressos = [0, 0, 0, 0, 0]
while True:
    sala = int(input("Sala (0 sai): "))
    if sala == 0:
        print("Fim")
        break
    if sala > len(lv) or sala < 1:
        print("Sala inválida")
    elif lv[sala - 1] == 0:
        print("Desculpe, sala lotada!")
    else:
        lugares = int(input(f"Quantos lugares você deseja ({lv[sala - 1]} vagos):"))
        if lugares > lv[sala - 1]:
            print("Esse número de lugares não está disponível.")
        elif lugares < 0:
            print("Número inválido")
        else:
            ingressos[sala - 1] += lugares
            lv[sala - 1] -= lugares
            print(f"{lugares} lugares vendidos")
    print("Utilização das salas")
    for sala, vagos in enumerate(lv):
        print(f"Sala {sala + 1} - {vagos} lugar(es) vazio(s)")
for sala, vendas in enumerate(ingressos):
    print(f"{vendas} ingressos vendidos na sala {sala + 1}")
for v in ingressos:
    vendas += v
print(vendas, "Ingressos vendidos")
