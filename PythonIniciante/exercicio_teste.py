# Escreva um programa que exiba uma lista de operações
# (menu): adição, subtração, divisão, multiplicação e sair.
# Imprima a tabuada da operação escolhida. Repita até que a
# opção saída seja escolhida.

saida = 1

while saida == 1:
    print("Menu: \n ")
    print(" 1 - Adição \n 2 - Subtração \n 3 - Divisão \n 4 - Multiplicação \n 5 - Saída \n")

    operacao = int(input("Escolha uma operação: "))

    if operacao == 1:
        tabuada = 1
        while tabuada <= 10:
            numero = 1
            while numero <= 10:
                print(f"{tabuada} + {numero} = {tabuada + numero}")
                numero += 1
            tabuada += 1
    if operacao == 2:
        tabuada = 1
        while tabuada <= 10:
            numero = 1
            while numero <= 10:
                print(f"{tabuada} - {numero} = {tabuada - numero}")
                numero += 1
            tabuada += 1
    if operacao == 3:
        tabuada = 1
        while tabuada <= 10:
            numero = 1
            while numero <= 10:
                print(f"{tabuada} / {numero} = {tabuada // numero}")
                numero += 1
            tabuada += 1
    if operacao == 4:
        tabuada = 1
        while tabuada <= 10:
            numero = 1
            while numero <= 10:
                print(f"{tabuada} x {numero} = {tabuada * numero}")
                numero += 1
            tabuada += 1

    if operacao == 5:
        saida -= 1
