vcarro = int(input("Velocidade do carro: "))
if vcarro > 80:
    multa = (vcarro - 80) * 5
    print(f"Você foi multado em R${multa} por ultrapassar limite de velocidade.")
