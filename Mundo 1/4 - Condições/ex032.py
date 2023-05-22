# Faça um programa que leia um ano qualquer e diga se o mesmo é bissexto.

from random import randint

x = randint(2024,5000)
print (f'O computador pensou no ano: {x}\n')

if x%4==0 and x%100!=0:
    print('Esse será um ano bissexto.')

else:
    print('Esse não será um ano bissexto.')