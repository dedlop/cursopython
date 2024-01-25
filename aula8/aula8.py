nome = 'Luiz'
idade = 32
altura = 1.80
peso = 80.5
ano_atual = 2022
nascimento = ano_atual - idade
imc = 80 / 1.8 ** 2

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso:.2f}kg.')
print(f'O IMC de {nome} é {imc:.2f}.')
print(f'{nome} nasceu em {nascimento}.')
