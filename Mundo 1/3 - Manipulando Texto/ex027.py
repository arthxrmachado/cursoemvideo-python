''' Faça um programa que leia o nome completo de uma pessoa e em seguida mostre o primeiro e último nome separadamente.

Exemplo: Ana Maria de Souza

Primeiro: Ana
Último: Souza '''

nome = str(input('Digite seu nome completo: ')).strip().split()

print(f'Primeiro nome: {nome[0]}')
print(f'Último nome: {nome[len(nome)-1]}')