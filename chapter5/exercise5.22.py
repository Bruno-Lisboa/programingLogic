while True:
    menu = input("Escolha: adição, subtração, multiplicação, divisão ou sair: ")
    if menu == "sair":
        break
    elif menu == "adição":
        ad = int(input("insira um número: "))
        count = 0
        while count <= 10:
            print(f"{ad} + {count} = {ad + count}")
            count += 1
    elif menu == "subtração":
        sub = int(input("insira um número: "))
        count = 0
        while count <= 10:
            print(f"{sub} - {count} = {sub - count}")
            count += 1
    elif menu == "multiplicação":
        mult = int(input("insira um número: "))
        count = 0
        while count <= 10:
            print(f"{mult} * {count} = {mult * count}")
            count += 1
    elif menu == "divisão":
        div = int(input("insira um número: "))
        count = 1
        while count <= 10:
            print(f"{div} / {count} = {div / count}")
            count += 1
    else:
        print("Faça uma escolha válida!")
