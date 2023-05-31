''' Faça um programa onde o usuário possa digitar 7 valores númericos e cadastre-os em uma lista única que mantenha
separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente. '''

valores = [[], []]

cont = 0

for i in range (0, 7):
    valor = (int(input(f'Digite o {i+1}º número: ')))

    if valor % 2 == 0:
       valores[0].append(valor)
    else:
        valores[1].append(valor)

valores[0].sort()
valores[1].sort()

print(f'\nValores pares: {valores[0]}')
print(f'Valores ímpares: {valores[1]}')