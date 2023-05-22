# Faça um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

from random import randint

n1 = randint(0,99)
n2 = randint(0,99)
n3 = randint(0,99)
print (f'O computador pensou nas retas: {n1}cm, {n2}cm e {n3}cm.\n')

if (n1+n2)>n3 and (n1+n3)>n2 and (n2+n3)>n1:
    print('Essas retas podem SIM formar um triângulo.')

else:
    print('Essas retas NÃO podem formar um triângulo')