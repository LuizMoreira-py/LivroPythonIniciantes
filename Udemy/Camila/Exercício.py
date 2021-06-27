"""
# Criar variáveis para nome (str), idade (int),
# altura (float) e peso (float) de uma pessoa
# Criar variável com o ano atual (int)
# Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
# Obter o IMC da pessoa com 2 casas decimantis (peso e na altura da pessoa)
# Exibir um texto com todos os valores da tela usando F-String (com as chaves)
"""

nome = 'Camila'
idade = 28
altura = 1.58
peso = 70
ano_atual = 2021
nascimento = ano_atual - idade
imc = (peso / ((altura * altura)))

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg.')
print(f'O IMC de Camila é {imc:.2f}.')
print(f'Camila nasceu em {2021-28}.')
