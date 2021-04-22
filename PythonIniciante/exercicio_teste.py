n1 = int(input("Informe um dividendo: "))
n2 = int(input(f"Informe um divisor para o número {n1} / "))

div = n1
cont = 0

while div > 0:
    div -= n2
    cont += 1
    print(f"Divisão {cont}: {div}")
