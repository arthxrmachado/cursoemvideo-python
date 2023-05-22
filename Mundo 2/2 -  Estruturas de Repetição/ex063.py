''' Faça um programa que leia um número n inteiro e mostre na tela os n primeiros elementos de uma Sequência de
Fibonacci.

Ex.: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8 '''

n = int(input('Digite um número: '))
cont = fib1 = 0
fib2 = 1

print(f'\nSegue abaixo os {n} primeiros números da Sequência de Fibonacci: ')

if n == 0:
    print(f'\nNada por aqui...')

elif n == 1:
    print(f'\n{fib1}')

else:
    print(f'\n{fib1} -> {fib2} ', end='-> ')
    while (cont<n-2):

        aux = fib2
        fib2 = fib1+fib2
        fib1 = aux

        print(f'{fib2} ', end='-> ')

        cont += 1

    print('')