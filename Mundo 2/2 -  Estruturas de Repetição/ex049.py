# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

num = int(input('Digite um número: '))

for i in range (1,11):
    print(f'{num} x {i} = {num*i}')