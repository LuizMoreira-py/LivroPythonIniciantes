nome = 'Camila Possebon'
idade = 28  # int
altura = 1.58  # float
e_maior = idade > 18  # bool
data_1 = True  # bool
data_atual = 2021
peso = 70
imc = (peso / altura ** 2)


print(nome, 'tem', idade, 'de idade e seu imc é', imc)

print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')

print('{0} tem {1} anos de idade e seu imc é {2}' .format(nome, idade, imc))

print('{n} tem {i} anos e seu imc é {im}'.format(n=nome, i=idade, im=imc))
