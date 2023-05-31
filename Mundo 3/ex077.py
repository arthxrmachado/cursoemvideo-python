''' Faça um programa que tenha uma tupla com várias palavras (não usar acentos). Depois, mostre para cada palavra, quais
são suas vogais. '''

tupla = ('Mouse', 'Cartao', 'Computador', 'Pendrive', 'Lapis', 'Caneta', 'Fone de Ouvido', 'Pulseira', 'Olho')

for i in tupla:
    print(f'\n{i}', end=' -> ')

    for letra in i:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')