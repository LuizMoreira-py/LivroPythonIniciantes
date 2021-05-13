# Escreva um programa que pergunte o valor inicial de uma dívida e o juro
# mensal. Pergunte também o valor mensal que será pago. Imprima o número
# de meses para que a dívida seja paga, o total pago e o total de juros pago.

divida = float(input("Valor divida: R$ "))
juros = float(input("Ex: 3 para 3%: "))
parcelas = float(input("Valor da parcela: R$ "))

mes = 1

if (divida * (juros / 100) > parcelas):
    print("Com esse valor você nunca vai terminar de pagar")
else:
    total = divida
    juros_total = 0

    while total > parcelas:
        juros = total * (juros / 100)
        total = total + juros - parcelas
        juros_total = juros_total + juros
        mes += 1
