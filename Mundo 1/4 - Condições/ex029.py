''' Faça um programa que leia a velocidade de um carro. Se o carro ultrapassar 80km/h, mostre uma mensagem dizendo
que o mesmo foi multado. A multa irá custar R$ 7,00 por cada km/h acima do limite. '''

from random import randint

x = randint(1,120)

print(f'O computador pensou no número: {x}\n')

if x>80:
    print('Você foi multado.\n')
    print(f'Valor da multa: R$ {(x-80)*7}')

else:
    print('Você está dentro da velocidade permitida.')