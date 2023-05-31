''' Faça um programa que crie uma matriz de dimensão 3x3 e preencha-a com valores lidos pelo teclado. No final, além de
colocar a matriz na tela com a formatação correta, mostre:

- A soma de todos os valores pares digitados;
- A soma dos valores da terceira coluna;
- O maior valor da segunda linha. '''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

pares = coluna3 = maior = 0

for l in range (0, 3):
    for c in range (0, 3):
        matriz[l][c] = int(input(f'Digite um valor para ({l}, {c}): '))
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
        if c == 2:
            coluna3 += matriz[l][c]
        if l == 1:
            if c == 0:
                maior = matriz[l][c]
            elif matriz[l][c] >= maior:
                maior = matriz[l][c]

print('')

for l in range (0, 3):
    for c in range (0, 3):
        print(f'{matriz[l][c]:^7}', end='')
    print('')

print(f'\nSoma dos valores pares: {pares}')
print(f'Soma dos valores da terceira coluna: {coluna3}')
print(f'Maior valor da segunda linha: {maior}')