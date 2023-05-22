# Faça um programa que o computador jogue pedra, papel e tesoura com você.

from random import randint

escolha = int(input('JOKENPÔ\n\n1 - Pedra\n2 - Papel\n3 - Tesoura\n\nEscolha um número: '))
print('')

computador  = randint(1,3)

if escolha==computador:
    if(escolha==1):
        print(f'EMPATE! Os dois jogadores escolheram PEDRA.')
    if (escolha == 2):
        print(f'EMPATE! Os dois jogadores escolheram PAPEL.')
    if (escolha==3):
        print(f'EMPATE! Os dois jogadores escolheram TESOURA.')

elif escolha==1 and computador==2:
    print(f'\VOCÊ PERDEU... Você escolheu PEDRA e o computador escolheu PAPEL.')

elif escolha==1 and computador==3:
    print(f'VOCÊ VENCEU! Você escolheu PEDRA e o computador escolheu TESOURA.')

elif escolha==2 and computador==1:
    print(f'VOCÊ VENCEU! Você escolheu PAPEL e o computador escolheu PEDRA.')

elif escolha==2 and computador==3:
    print(f'VOCÊ PERDEU... Você escolheu PAPEL e o computador escolheu TESOURA.')

elif escolha==3 and computador==1:
    print(f'VOCÊ PERDEU... Você escolheu TESOURA e o computador escolheu PEDRA.')

elif escolha==3 and computador==2:
    print(f'VOCÊ VENCEU! Você escolheu TESOURA e o computador escolheu PAPEL.')

else:
    print(f'Escolha um número válido.')