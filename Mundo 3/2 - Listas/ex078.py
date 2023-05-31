''' Faça um programa que leia 5 valores númericos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor
valor digitado e as suas respectivas posições na lista. '''

valores = list()
#valores = list[]
maior = menor = 0

for i in range (0, 5):
    valores.append(int(input('Digite um valor: ')))

    if i == 0:
        maior = menor = valores[i]
    else:
        if valores[i] > maior:
            maior = valores[i]
        elif valores[i] < menor:
            menor = valores[i]

print(f'\nMaior valor: {maior} -> Posições: ', end='')
for a, b in enumerate (valores):
    if b == maior:
        print(f'{a}', end=' ')

print(f'\nMenor valor: {menor} -> Posições: ', end='')
for a, b in enumerate (valores):
    if b == menor:
        print(f'{a}', end=' ')

print('')