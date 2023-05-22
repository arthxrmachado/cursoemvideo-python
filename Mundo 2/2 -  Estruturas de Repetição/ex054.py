''' Faça um programa que leia o ano de nascimento de 7 pessoas. No final, mostre quantas pessoas ainda não atingiram a
maioridade e quantas pessoas já atingiram. '''

from datetime import date

maior = 0
menor = 0

ano_atual = date.today().year

for i in range (0, 7):

    ano_nascimento = int(input('Digite o ano de seu nascimento: '))

    if ano_atual - ano_nascimento >= 18:
        maior += 1
    else:
        menor += 1

print(f'\nPessoas que já atingiram a maioridade: {maior}\nPessoas que não atingiram a maioridade: {menor}')