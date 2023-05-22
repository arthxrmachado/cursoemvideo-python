''' Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude-o, lendo os
nomes de seus alunos e mostrando na tela o nome escolhido. '''

from random import choice

n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')

lista = [n1, n2, n3, n4]

print(f'O aluno escolhido foi: {choice(lista)}')
