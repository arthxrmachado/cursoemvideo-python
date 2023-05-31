''' Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão
gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta. '''

from random import randint
from time import sleep

num = cont = 0
temp = []
princ = []
jogos = int(input('Digite a quantidade de jogos que deseja gerar: '))

for i in range (0, jogos):

    while True:
        num = randint(1, 10)

        if num not in temp:
            temp.append(num)
            cont += 1

        if cont >= 6:
            break

    cont = 0
    temp.sort()
    princ.append(temp[:])
    temp.clear()

print('')
for i, j in enumerate(princ):
    print(f'Jogo {i+1}: {j}')
    sleep(1)