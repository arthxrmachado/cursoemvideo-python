''' Faça um programa que tenha uma tupla com várias palavras (não usar acentos). Depois, mostre para cada palavra, quais
são suas vogais. '''

tupla = ('Mouse', 'Cartao', 'Computador', 'Pendrive', 'Lapis', 'Caneta', 'Fone de Ouvido', 'Pulseira', 'Olho')

for i in range (0, len(tupla)):
    print(f'\n{tupla[i]}', end=' -> ')
    for c in tupla[i]:
        if c in 'AEIOUaeiou':
            print(c, end=' ')