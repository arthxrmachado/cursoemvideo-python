''' Faça um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa
progressão. '''

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite uma razão: '))
delimitador = termo + (10 - 1) * razao

for i in range (termo, delimitador + razao, razao):
    print(i)