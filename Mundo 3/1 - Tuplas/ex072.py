''' Faça um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.

Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso. '''

extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
           'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

num = int(input('Digite um número inteiro (de 0 até 20): '))

while num>20 or num<0:
    print('\nNúmero inválido! Tente novamente.')
    num = int(input('\nDigite um número inteiro (de 0 até 20): '))

print(f'\n{extenso[num]}')