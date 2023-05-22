''' Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos seus dígitos separados.

Exemplo:

Número: 1834

Unidade: 4
Dezena: 3
Centena: 8
Milhar: 1. '''

num = int(input('Digite um número: '))

unidade = num//1%10
dezena = num//10%10
centena = num//100%10
milhar = num//1000%10

print(f'\nUnidade: {unidade}\nDezena: {dezena}\nCentena: {centena}\nMilhar: {milhar}')