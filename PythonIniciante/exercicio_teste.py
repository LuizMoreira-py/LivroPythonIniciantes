deposito = float(input("Digito o valor do depósito: R$ "))
taxa = float(input("Digite o valor da taxa: R$ "))



mes = 0

while mes <= 24:
    total = deposito * taxa
    juros = total * mes
    mes += 1
    print(f"Mês {mes} Deposito {total} Rendimento {juros}")
