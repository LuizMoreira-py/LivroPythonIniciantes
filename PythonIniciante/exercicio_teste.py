n1 = int(input("Digite o número que deseja dividir: "))
n2 = int(input(f"Digite quantas vezes deseja dividir o número {n1}: "))

div = n1


while div >= 0:
    div -= n2
print(f"Total: {div}")
