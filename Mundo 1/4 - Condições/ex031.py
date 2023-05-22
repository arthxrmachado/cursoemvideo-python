''' Faça um programa que pergunte a distância de uma viagem em quilômetros. Calcule o preço da passagem cobrando R$ 0,50
por quilômetro para viagens de até 200km ou R$ 0,45 para viagens mais longas. '''

from random import randint

x = randint(50,450)

print(f'Esta viagem terá: {x} quilômetros.\n')

if x>200:
    print(f'Valor total da viagem: R$ {x*0.45:.2f}')

else:
    print(f'Valor total da viagme: R$ {x*0.50:.2f}')