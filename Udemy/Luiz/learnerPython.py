numero = input("Digite um número inteiro: ")

if numero.isdigit():
    numero = int(numero)
    if numero % 2 == 0:
        print("O número digitado é par!")
    elif numero % 2 == 1:
        print("O número digitado é impar!")
else:
    print("O valor digitado não é inteiro!")

horas = int(input("Digite somente a hora do seu relógiio: "))

if horas <= 11:
    print("Bom dia!")
elif horas >= 12 and horas <= 17:
    print("Boa tarde!")
else:
    print("Boa noite!")
