''' Faça um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final,
mostre uma listagem de preços, organizando os dados em forma tabular. '''

produtos = ('Geladeira', 2499.99, 'Fogão', 999.00, 'Cama de Solteiro', 599.00, 'Cama de Casal', 1199.89, 'Mesa de Jantar',
            499.99, 'Micro-Ondas', 479.29)

print('-'*40)
print(f'{"PREÇOS":^40}')
print('-'*40)

for i in range (0, len(produtos)):
    if i%2 == 0:
        print(f'{produtos[i]:.<30}', end='')
    else:
        print(f'R$ {produtos[i]:>7.2f}')

print('-'*40)