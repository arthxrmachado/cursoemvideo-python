# Faça um programa que leia o nome completo de uma pessoa e verifique se existe a palavra "Lourenço" nesse nome.

nome = str(input('Digite seu nome completo: ')).strip()

if 'lourenço' in nome.lower():

    print('\nExiste a palavra "Lourenço" em seu nome.')

else:

    print('\nNão existe a palavra "Lourenço" em seu nome.')