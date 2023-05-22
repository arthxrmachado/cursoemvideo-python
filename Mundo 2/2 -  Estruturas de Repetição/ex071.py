''' Faça um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor
a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.

ps.: Considere que o caixa possui cédulas de R$ 50,00, R$ 20,00, R$ 10,00 e R$ 1,00. '''

notas50 = notas20 = notas10 = notas1 = 0

valor = int(input('Digite o valor que deseja sacar: '))

f'\nValor: R$ {valor}\n'

notas50 = valor//50
valor = valor%50

notas20 = valor//20
valor = valor%20

notas10 = valor//10
valor = valor%10

notas1 = valor//1

print(f'\nNotas de 50: {notas50}'
      f'\nNotas de 20: {notas20}'
      f'\nNotas de 10: {notas10}'
      f'\nNotas de 1: {notas1}')