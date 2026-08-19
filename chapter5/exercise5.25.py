# infelizmente não consegui fazer o exercicio 5.25
# tiver que copiar do site

n = float(input("Digite um número para encontrar sua raiz quadrada: "))
b = 2
while abs(n - (b * b)) > 0.00001:
    p = (b + (n / b)) / 2
    b = p
print(f"A raiz de {n} é aproximadamente {p:4f}")

# nesse momento do livro o conceito de "abs" como ta ali na condição do while
# ainda não tinha sido apresentada, então não tinha nem como eu fazer esse exercicio
