''' Faça um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
No final, mostre:

a) qual é o total gasto na compra.
b) quantos produtos custam mais de R$ 1000,00.
c) qual é o nome do produto mais barato.'''

total = produtosMC = nomeMB = precoMB = 0

while True:
    nome = str(input('Digite o nome do produto: ')).upper()
    preco = float(input('Digite o preço desse produto: '))

    nomeMB = ''
    precoMB = preco
    total += preco

    if preco > 1000.00:
        produtosMC += 1

    if preco <= precoMB:
        precoMB = preco
        nomeMB = nome

    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('\nDeseja continuar? [S/N]: ')).strip().upper()[0]

    print('')

    if escolha == 'N':
        break

print(f'Total gasto: R$ {total:.2f}'
      f'\nProdutos que custam mais que R$ 1000,00: {produtosMC}'
      f'\nNome do produto mais barato: {nomeMB}')
