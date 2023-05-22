''' Escreva um jogo que faça o computador pensar em um número inteiro entre 1 e 10 e peça para o usuário adivinhar que
número o mesmo está pensando. O jogo deve continuar até o usuário acertar o número que o computador está pensando e no
final deve mostrar quantos palpites foram necessários até o acerto'''

from random import randint

y = randint(1,10)
x = palpite = 0

while x != y:

    x = int(input('Digite um número de 1 a 10: '))

    print(f'\nO computador pensou no número: {y}\n')

    if x==y:
        print('Parabéns, você acertou!')

    else:
        print('Infelizmente você errou...\n')

    palpite += 1

if palpite == 1:
    print('Só precisou de somente uma tentativa!')

else:
    print (f'Foram necessários {palpite} palpites até você vencer o jogo.')