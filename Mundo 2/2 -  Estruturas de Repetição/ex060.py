''' Faça um programa que leia um número e mostre seu fatorial.

Ex.: 5! = 5x4x3x2x1 = 120. '''

num = int(input('Digite um número: '))
print(f'\nNúmero digitado: {num}')
fatorial = num

if num == 0 or num < 0:
    print('\nNúmero inválido.')

else:
    while num != 1:
        num -= 1
        fatorial *= num

print(f'O fatorial desse número é: {fatorial}')

#   usando a biblioteca math

#   from math import factorial
#   num = int(input('Digite um número: '))
#   f = factorial(num)

#   print(f'O fatorial de {num} é {f}.')