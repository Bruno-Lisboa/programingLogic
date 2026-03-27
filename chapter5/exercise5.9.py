n1 = int(input("dividendo: "))
n2 = int(input("divisor: "))
result = 0
while n1 >= n2:
    n1 = n1 - n2
    result = result + 1
print(f"Resultado: {result}")
print(f"Resto: {n1}")
