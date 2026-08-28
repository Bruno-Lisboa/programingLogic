# program 6.7, pg 163. portuguese version of the book (4th ediction)
# program modified to only exit when "S" is typed, and accpet string like FFFFFFAAAAAAS at once.

último = 10
fila = list(range(1, último + 1))
x = 0
fim = ""
while True:
    print(f"\nExistem {len(fila)} clientes na fila")
    print("Digite F para adicionar um cliente ao fim da fila,")
    print("ou A para realizar o atendimento. S para sair.")
    operação = list(input("Operação (F, A ou S):"))
    while x < len(operação):
        if operação[x] == "A":
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f"Cliente {atendido} atendido")
            else:
                print("Fila vazia! Ninguém para atender.")
        elif operação[x] == "F":
            último += 1 # Incrementa o ticket do novo cliente
            fila.append(último)
        elif operação[x] == "S":
            fim = "S"
            break
        else:
            print("Operação inválida! Digite apenas F, A ou S!")
        x += 1
    if fim == "S":
        break
    else:
        x = 0
