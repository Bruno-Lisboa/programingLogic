#Programa que pede o valor de uma merdaria e o desconto
mercadoria = float(input("Adicione o preço:"))
desconto = float(input("Adicione a porcentagem de desconto:"))
resultado = mercadoria * (desconto/100)
resultadoFinal = mercadoria - resultado
print(f"Valor original: R${mercadoria:.2f}")
print(f"Desconto aplicado: R${resultado:.2f}")
print(f"Preço final: R${resultadoFinal:.2f}")
