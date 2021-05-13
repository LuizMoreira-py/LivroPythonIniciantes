# Escreva um programa que pergunte o valor inicial de uma dívida e o juro
# mensal. Pergunte também o valor mensal que será pago. Imprima o número
# de meses para que a dívida seja paga, o total pago e o total de juros pago.

divida = float(input("Valor divida: R$ "))
taxa = float(input("Ex: 3 para 3%: "))
parcelas = float(input("Valor da parcela: R$ "))

mes = 1

if (divida * taxa / 100 > parcelas):
    print("Com esse valor você nunca vai terminar de pagar")
else:
    total = divida
    juros_total = 0

    while total > parcelas:
        juros = total * taxa / 100
        total = total + juros - parcelas
        juros_total = juros_total + juros
        print(f"Total da dívida no mês {mes} é de R$ {total:6.2f}")
        mes += 1

    print(
        f"Para pagar uma dívida de R${divida:8.2f}, a {taxa:5.2f} % de juros")
    print(
        f"você precisará de {mes - 1} meses, pagando um total de R${juros_total:8.2f} de juros.")
    print(
        f"No último mês, você teria um saldo residual de R${total:8.2f} a pagar.")
