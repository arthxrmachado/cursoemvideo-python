''' Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, em seguida
calcule e mostre o comprimento da hipotenusa. '''

from math import hypot

co = float(input('Digite o tamanho do cateto oposto: '))
ca = float(input('Digite o tamanho do cateto adjacente: '))

print(f'A hipotenusa irá medir: {hypot(co, ca):.2f}')
