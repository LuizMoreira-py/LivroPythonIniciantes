# Escreva um programa que leia números inteiros do teclado. O programa deve
# ler os números até que o usuário digite 0 (zero). No final da execução,
# exiba a quantidade de números digitados como a soma e a média aritmética.

contador = 0
soma = 0
while True:
    numeros = int(input("Digitite um número inteiro: "))
    if numeros == 0:
        break
    soma += numeros
    
    contador += 1

print(f"Total de números digitados: {contador}")
print(f"Soma: {soma}")
