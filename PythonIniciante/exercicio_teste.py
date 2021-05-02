mes = 0

deposito = float(input())
taxa = float(input())

rendimento = deposito * taxa

while mes <= 23:
    rendimentoPeriodo = (deposito * taxa) * mes
    rendiimentoTotal = deposito + rendimentoPeriodo
    mes += 1
    print(f"Mês {mes} ---- Depósito: R$ {deposito:6.2f} ---- Rendimento: R$ {rendimento:6.2f} ---- Rendimento periodo: R$ {rendimentoPeriodo:6.2f} ---- Rendimento total: {rendiimentoTotal:6.2f}")
