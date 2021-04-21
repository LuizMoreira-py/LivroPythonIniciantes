n1 = int(input("Digite um número inteiro: "))
multi = int(input(f"Digite quantas vezes deseja somar o número {n1} x "))

n = 1
soma = 0
cont = 0

while n <= multi:
    soma = soma + n1
    n = n + 1
    cont += 1
    print(f"Soma {cont}: {n1} + {soma}")
