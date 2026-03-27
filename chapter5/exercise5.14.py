count = 0
soma = 0
while True:
    number = int(input("Type a integer number or 0 to progress: "))
    if number == 0:
        break
    soma += number
    count += 1
print(f" {count} Numbers were typed!")
print(f" Soma: {soma}")
print(f" Média: {soma / count}")
