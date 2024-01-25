nome  = 'Luiz Otávio'
idade = 32
altura = 1.80
e_idade = idade > 18
peso = 80
imc = peso / (altura ** 2)

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{} tem {} anos e seu imc é {}'.format(nome, idade, imc))