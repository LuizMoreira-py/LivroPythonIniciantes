# Altere o programa anterior de forma a perguntar também o valor depositado
# mensalmente. Esse valor será depositado no início de cada mês, e você
# deve considerá-lo para o cálculo de juros do mês seguinte.

deposito = float(input("Depósito inicial: R$ "))
taxa = float(input("Ex: 3 para 3.0%: "))
investimento = float(input("Depósito mesnsal: R$ "))

mes = 0
saldo = deposito

while mes <= 23:
    saldo = saldo + (saldo * (taxa / 100)) + investimento
    mes += 1
    print(f"Mês {mes} - Rendimento: R$ {saldo:6.2f}")

print(f"Rendimento total: R$ {saldo - deposito:6.2f}")
