# Faça um programa que leia um número inteiro e diga se ele é primo ou não.

num = int(input('Digite um número: '))
cont = 0

for i in range (1, num+1):
    if num%i == 0:
        print('\033[34m', end=' ')
        cont += 1
    else:
        print('\033[31m', end=' ')
    print(f'{i}', end=' ')

if cont == 2:
    print(f'\n\n\033[mO número {num} é primo.')

else:
    print(f'\n\n\033[mO número {num} não é primo.')
    print(f'Esse número foi dividido {cont} vezes.')