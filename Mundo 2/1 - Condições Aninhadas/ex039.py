''' Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

- Se ele ainda vai se alistar ao serviço militar;
- Se é hora de se alistar;
- Se já passou do tempo de alistamento.

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo. '''

from datetime import date

ano_atual = date.today().year

ano_nascimento = int(input('Digite o ano de seu nascimento: '))

idade = ano_atual - ano_nascimento

print(f'\nQuem nasceu em {ano_nascimento} tem {idade} anos em {ano_atual}.\n')

if idade < 18:
    print(f'Você ainda irá se alistar. Faltam {18-idade} anos.')

elif idade > 18:
    print(f'Já passou do tempo de seu alistamento. Você está {idade-18} anos atrasado.')

else:
    print('Está na hora de se alistar.')