''' Faça um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista na posição correta
de inserção (sem utilizar o método sort()). No final, mostre a lista ordenada na tela. '''

valores = list()
#valores = list[]

for i in range (0, 5):
    valor = int(input('Digite um valor: '))

    if i == 0 or valor > valores[-1]:
        valores.append(valor)
        print(f'Valor adicionado no final da lista.')

    else:
        cont = 0
        while cont < len(valores):
            if valor <= valores[cont]:
                valores.insert(cont, valor)
                print(f'Valor adicionado na {cont}ª posição da lista.')
                break
            cont += 1

print(f'\nValores digitados em ordem: {valores}')