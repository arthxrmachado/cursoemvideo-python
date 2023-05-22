''' Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. '''

from random import randint

vitoria = 0

while True:

    computador = randint(0, 10)
    escolha = str(input('Escolha entre PAR ou ÍMPAR: ')).strip().upper()
    jogador = int(input('Digite um número inteiro [0 até 10]: '))

    print(f'\nVocê jogou: {jogador}\nO computador jogou: {computador}')

    #par
    if (jogador+computador)%2 == 0:
        #se a escolha do jogador for par
        if escolha == 'PAR' or escolha == 'P':
            print('\nParabéns, você venceu!')
            print('')
            vitoria += 1

        #se a escolha do jogador for ímpar
        else:
            print('\nVocê perdeu...')
            break

    #ímpar
    elif (jogador+computador)%2 != 0:
        #se a escolha do jogador for ímpar
        if escolha == 'IMPAR' or escolha == 'ÍMPAR' or escolha == 'I':
            print('\nParabéns, você venceu!')
            print('')
            vitoria += 1

        #se a escolha do jogador for par
        else:
            print('\nVocê perdeu...')
            break

    #se a escolha não for par e nem ímpar
    else:
        print('\nOpção inválida.')

print(f'\nSeu número de vitórias: {vitoria}')