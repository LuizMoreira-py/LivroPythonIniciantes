# Escreva um programa que leia um número e verifique se é ou não um
# número primo. Para fazer essa verificação, calcule o resto da
# divisão do número por 2 e depois por todos os números ímpares
# até o número lido. Se o resto de uma dessas divisões for igual zero,
# o número não é primo. Observe que 0 e 1 não são primos e que 2 é o único
# número primo que é par.

numero = int(input())
resto = numero % 2
print(resto)

x = 1
while x <= numero:
    impar = x
    if impar % 2 == 1:
        print(impar)
    x += 1
    while True:
        primo = numero // impar
        if primo > 0 and primo != 0:
            print("Primo")
        else:
            print("Não primo")
        break
