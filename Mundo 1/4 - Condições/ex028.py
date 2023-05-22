''' Escreva um jogo que faça o computador pensar em um número inteiro entre 1 e 5 e peça para o usuário adivinhar que
número o mesmo está pensando. O programa deverá escrever na tela se o usuário venceu ou perdeu o jogo. '''

from random import randint

x = int(input('Digite um número de 1 a 5: '))

y = randint(1,5)

print(f'\nO computador pensou no número: {y}\n')

if x==y:
    print('Parabéns, você acertou!')

else:
    print('Infelizmente você errou...')