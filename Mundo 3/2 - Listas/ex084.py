''' Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre:

- Quantas pessoas foram cadastradas;
- Uma listagem com as pessoas mais pesadas;
- Uma listagem com as pessoas mais leves. '''

pessoa = list()
total = list()
pesada = list()
leve = list()

while True:
    pessoa.append(str(input('Digite o nome da pessoa: ')))
    pessoa.append(float(input('Digite seu peso: ')))

    if pessoa[1] >= 100:
        pesada.append(pessoa[:1])

    elif pessoa[1] <= 50:
        leve.append(pessoa[:1])

    total.append(pessoa[:])

    pessoa.clear()

    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]

    if opcao == 'N':
        break

print(f'\nVocê cadastrou {len(total)} pessoas.')
print(f'As pessoas mais pesadas são: {pesada}')
print(f'As pessoas mais leves são: {leve}')