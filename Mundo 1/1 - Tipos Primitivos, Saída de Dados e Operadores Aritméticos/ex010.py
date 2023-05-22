# Faça um programa que leia o preço de um produto e aplique 5% de desconto.

preco = float(input('Digite o preço do produto: '))

print(f'Preço do produto: R${preco:.2f}\nPreço com 5% de desconto: R${preco-preco*5/100:.2f}.')
