valor = 1

while valor >= 0:
    valor = float(input("Digite o valor a pagar: "))
    cedulas = 0
    atual = 100.00
    apagar = valor
    if valor == 0:
        break


    while True:
        if atual <= apagar:
            apagar -= atual
            cedulas += 1

        else:
            if atual >= 1:
                print(f"{cedulas} cédula(s) de R${atual}")
            else:
                print(f"{cedulas} moeda(s) de R${atual:5.2f}")

            if apagar == 0.01:
                break
            elif atual >= 100:
                atual = 50
            elif atual >= 50:
                atual = 20
            elif atual >= 20:
                atual = 10
            elif atual >= 10:
                atual = 5
            elif atual >= 5:
                atual = 2
            elif atual >= 2:
                atual = 1
            elif atual >= 1:
                atual = 0.50
            elif atual >= 0.50:
                atual = 0.25
            elif atual >= 0.25:
                atual = 0.10
            elif atual >= 0.10:
                atual = 0.05
            elif atual >= 0.05:
                atual = 0.01
            else:
                atual = 0.01
                break
            cedulas = 0
