# variaveis
val1 = 0
val2 = 0
tot = 0
operator = 0
escolha = 7
exit = 2

#corpo
while exit != 0:
    escolha = int(input("\nescolha a forma da operação \n[1] Adição +\n[2] Subtração -\n[3] Multiplicação *\n[4] Divisão /\n[5] Finalizar o Codigo\n"))

    if escolha > 6 or escolha < 1:
        escolha = int(input(
            "\nnumero invalido, escolha a forma da operação \n[1] Adição +\n[2] Subtração -\n[3] Multiplicação *\n[4] Divisão /\n[5] Finalizar o Codigo\n"))
    elif escolha == 1:
        print("\nVocê escolheu adição")
    elif escolha == 2:
        print("\nVocê escolheu subtração")
    elif escolha == 3:
        print("\nVocê escolheu Multiplicação")
    elif escolha == 4:
        print("\nVocê escolheu Divisão")
    elif escolha == 5:
        exit = 0

    if exit != 0:
        val1 = int(input("\nDigite o primeiro numero desejado!\n"))
        val2 = int(input("\nDigite o segundo numero desejado!\n"))
        if escolha == 1:
            tot = val1 + val2
        elif escolha == 2:
            tot = val1 - val2
        elif escolha == 3:
            tot = val1 * val2
        elif escolha == 4:
            tot = val1 / val2

        print("\nO resultado é {}\n".format(tot))

    if exit != 0:
        exit = int(input(""" Escolha uma das opções!!
[0] Para finalizar o programa.
[1] Para realizar outro calculo.
\n"""))

print("Agradecemos por utilizar nossa Calculadora!!\n\n")