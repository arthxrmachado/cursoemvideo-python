# Faça um programa que leia um número real qualquer e mostre na tela sua porção inteira.

from math import trunc

n1 = float(input('Digite um número: '))

print (f'Número digitado: {n1}\nPorção inteira: {trunc(n1)}')
