''' Faça um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final,
mostre uma listagem de preços, organizando os dados em forma tabular. '''

produtos = ('Geladeira', 2499.99, 'Fogão', 999.00, 'Cama de Solteiro', 599.00, 'Cama de Casal', 1199.89, 'Mesa de Jantar',
            499.99, 'Micro-Ondas', 479.29)

for i in range (0, len(produtos)):
    if i % 2 == 0:
        print(f'{produtos[i]} - R$ {produtos[i+1]:.2f}')