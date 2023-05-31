''' Faça um programa que leia vários números e coloque-os em uma lista. Depois disso, crie duas listas extras que vão
conter apenas os valores pares e ímpares, respectivamente. Ao final, mostre o conteúdo das três listas geradas. '''

valores = list()
pares = list()
impares = list()
#valores = list[]

while True:
    valores.append(int(input('Digite um valor: ')))

    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]

    if opcao == 'N':
        break

for i in valores:
    if i%2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print(f'\nLista completa: {valores}')
print(f'Lista de pares: {pares}')
print(f'Lista de ímpares: {impares}')