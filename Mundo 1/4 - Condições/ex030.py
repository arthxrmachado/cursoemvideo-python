# Faça um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.

from random import randint

x = randint(0,999)
print(f'O computador pensou no número: {x}\n')

if x%2 == 0:
    print('Esse número é par.')

else:
    print('Esse número é ímpar.')