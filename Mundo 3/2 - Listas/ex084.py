''' Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre:

- Quantas pessoas foram cadastradas;
- Uma listagem com as pessoas mais pesadas;
- Uma listagem com as pessoas mais leves. '''

#criando uma lista temporária para armazenar dados
temp = list()
#criando a lista principal
pessoas = list()
maior = menor = 0

while True:
    temp.append(str(input('Digite o nome da pessoa: ')))
    temp.append(float(input('Digite seu peso: ')))

    if len(pessoas) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        elif temp[1] < menor:
            menor = temp[1]

    #passando dados para a lista principal
    pessoas.append(temp[:])
    #limpando a lista temporária
    temp.clear()

    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]

    if opcao == 'N':
        break

    print('')

print(f'\nForam cadastradas {len(pessoas)} pessoas.')

print(f'Maior peso: {maior} kg -> Peso de:', end='')
for i in pessoas:
    if i[1] == maior:
        print(f' {i[0]}', end='')

print(f'\nMenor peso: {menor} kg -> Peso de:', end='')
for i in pessoas:
    if i[1] == menor:
        print(f' {i[0]}', end='')