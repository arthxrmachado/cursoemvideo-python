# Faça um programa que leia três números e mostre qual é o maior e o menor.

from random import randint

n1 = randint(0,99)
n2 = randint(0,99)
n3 = randint(0,99)

print (f'O computador pensou nos números: {n1}, {n2} e {n3}.\n')

#verificando o menor número
menor = n1

if n2 < n1 and n2 < n3:
    menor = n2

if n3 < n1 and n3 < n2:
    menor = n3

#verificando o maior número
maior = n1

if n2 > n1 and n2 > n3:
    maior = n2

if n3 > n1 and n3 > n2:
    maior = n3

print (f'Maior: {maior}\nMenor: {menor}')
