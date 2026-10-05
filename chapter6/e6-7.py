# esse exercício foi um marco, quase me fez desistir. foi disparado o mais difícil de todos até o momento
# depois de mais de 3 semanas eu consegui superar esse obstáculo que foi um verdadeiro terror, mas ao mesmo tempo muito importante
# para evoluir meu entedimento de lógica de programação!
expre = []
text = input("Digite a expressão: ")
expre.extend(text)
pilha = []
x = 0
erro = 0
while True:
    if len(expre) < x + 1:
        break
    else:
        if expre[x] == "(":
            pilha.append("y")
        elif expre[x] == ")":
            if len(pilha) == 0:
                erro = 1
                break
            else:
                pilha.pop(len(pilha) - 1)
        else:
            erro = 1
            break
        x += 1

if len(pilha) > 0:
    erro = 1
if len(text) == 0:
    erro = 2

if erro == 1:
    print(f"{text} Erro")
elif erro == 2:
    print("Você saiu do programa!")
else:
    print(f"{text} OK")
