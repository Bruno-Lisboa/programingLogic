print("Calculadora que mostra o resto de uma divisão.")
dndo = int(input("Digite um número para ser o dividendo: "))
dsor = int(input("Digite um número para ser o divisor: "))
calc = 0
while dndo > calc:
    calc += dsor
    if calc > dndo:
        calc -= dsor
        break
print(f"O resto da divisão é: {dndo - calc}")
