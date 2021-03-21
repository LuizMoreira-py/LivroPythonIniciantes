velocidadeCarro = int(input("Informe a velocidade do carro: "))
multa = float(5)

if velocidadeCarro > 80:
    exedente = velocidadeCarro - 80
    valorMulta = exedente * multa

    print("Você foi multado!")
    print("O valor da multa é R$ {:5.2f}". format(valorMulta))
