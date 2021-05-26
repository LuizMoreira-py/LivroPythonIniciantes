# Escreva um programa que leia um número e verifique se é ou não um
# número primo. Para fazer essa verificação, calcule o resto da
# divisão do número por 2 e depois por todos os números ímpares
# até o número lido. Se o resto de uma dessas divisões for igual zero,
# o número não é primo. Observe que 0 e 1 não são primos e que 2 é o único
# número primo que é par.


numero = int(input())

resto = numero % 2
cont = 1

if numero == 0:
    print("Valor invalido!")
    numero = int(input())
while cont <= numero:
    divisao = resto // cont
    cont += 1

if divisao == 0:
    print("Não é primo!")
else:
    print("Primo!")
