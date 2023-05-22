''' Faça um programa que leia 6 números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado
for ímpar, desconsidere-o. '''

soma = 0

for i in range(0, 6):
    num = int(input('Digite um número inteiro: '))
    if num%2 == 0:
        soma += num
print(f'\nA soma de todos os valores digitados foi: {soma}')