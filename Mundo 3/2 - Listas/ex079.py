''' Faça um programa onde o usuário possa digitar vários valores númericos e cadastre-os em uma lista. Caso o número já
exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''

valores = list()
#valores = list[]

while True:

    valor = int(input('Digite um valor: '))

    if valor in valores:
        print(f'\nEsse valor já está na lista. Valor não adicionado.')
    else:
        valores.append(valor)

    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('\nDeseja continuar? [S/N]: ')).upper().strip()[0]

    if opcao == 'N':
        break

    print('')

print(f'\nLista: {sorted(valores)}')