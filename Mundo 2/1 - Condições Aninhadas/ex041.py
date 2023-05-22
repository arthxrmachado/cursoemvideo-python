''' Faça um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com sua idade:

- Até 9 anos: MIRIM;
- Até 14 anos: INFANTIL;
- Até 19 anos: JÚNIOR;
- Até 25 anos: SÊNIOR;
- Acima: MASTER. '''

from datetime import date

ano_atual = date.today().year

ano_nascimento = int(input('Digite o ano de seu nascimento: '))

idade = ano_atual - ano_nascimento

if idade <= 9:
    print('\nEste atleta faz parte da categoria MIRIM.')

elif idade <= 14:
    print('\nEste atleta faz parte da categoria INFANTIL.')

elif idade <= 19:
    print('\nEste atleta faz parte da categoria JÚNIOR.')

elif idade <= 25:
    print('\nEste atleta faz parte da categoria SÊNIOR.')

else:
    print('\nEste atleta faz parte da categoria MASTER.')