"""
Iniciar com letra, pode conter números, separar _, letras minúsculas
"""
nome = 'Camila Possebon'
idade = 28  # int
altura = 1.58  # float
e_maior = idade > 18  # bool
data_1 = True  # bool
data_atual = 2021
peso = 70
imc = (peso / altura ** 2)

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('É de maior', e_maior)
print('IMC', imc)

print(idade * altura)

print(nome, 'tem', idade, 'de idade e seu imc é', imc)
