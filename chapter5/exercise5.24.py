# repetidor de números primos
n = int(input("Digite a quantidade de número primos que deseja ver: "))
primo = 3
impar = 3
repeater = 1
if n == 1:
    print(2)
else:
    repeater = 2
    print(2)
while repeater <= n:
    if primo == 3:
        print(primo)
        repeater += 1
        primo += 2
    while impar < primo:
        if primo % impar == 0:
            primo += 2
            impar = 3
        else:
            impar += 2
    print(primo)
    impar = 3
    repeater += 1
    primo += 2
