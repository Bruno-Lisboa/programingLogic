d = int(input("Depósito inicial: "))
tj = float(input("Taxa de juros: "))
j = 0 #juros
c = 1 # contador
while c <= 24:
    d = d + (d * (tj/100))
    print(f"Poupança no mês {c}: {d:.2f}")
    j = j + (d * (tj/100)) 
    c = c + 1
print(f"Valor total acumulado em {c - 1} meses: {d:.2f}")
print(f"Juros total acumulado: {j:.2f}")
