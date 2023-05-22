''' Faça um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa
progressão. '''

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite uma razão: '))

contador = 0
while contador < 10:

    print(termo)
    termo += razao

    contador += 1

print('\nFim!')