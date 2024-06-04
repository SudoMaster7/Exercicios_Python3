nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
ano_atual = 2024
ano_nascimento = ano_atual - idade
imc = peso / (altura ** 2)

print(f'\nOlá {nome} seus dados são: \n'
      f'Ano de Nascimento: {ano_nascimento}\n'
      f'Idade: {idade}\n'
      f'Peso: {peso:.2f}\n'
      f'Altura: {altura:.2f}\n'
      f'IMC: {imc:.2f}\n')
