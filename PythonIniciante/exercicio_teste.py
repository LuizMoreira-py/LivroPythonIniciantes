# Escreva um programa que leia um número e verifique se é ou não um
# número primo. Para fazer essa verificação, calcule o resto da
# divisão do número por 2 e depois por todos os números ímpares
# até o número lido. Se o resto de uma dessas divisões for igual zero,
# o número não é primo. Observe que 0 e 1 não são primos e que 2 é o único
# número primo que é par.

fim = int(input("Informe um número para ver se ele é primo: "))
resto = fim % 2

x = fim
while True:
    primo = x % 2 // impar
    if primo > 0 and primo != 1:
        print("É primo")
    else:
        print("Não é primo")
    break
