deposito = float(input("Digito o valor do depósito: "))
taxa = float(input("Digite o valor da taxa: "))



mes = 0
total = deposito * taxa

while mes <= 24:
    juros = total * mes    
    mes += 1
    print(f"Mês {mes} Deposito {deposito} Rendimento {juros}")
