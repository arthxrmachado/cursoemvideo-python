''' Faça um programa que leia quatro valores pelo teclado e armazene-os em uma tupla. No final, mostre:

- Quantas vezes apareceu o valor 9;
- Em que posição foi digitado o primeiro valor 3;
- Quais foram os números pares. '''

tupla = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')),
         int(input('Digite um número: ')))
cont9 = cont3 = contPar = 0

for i in range (0, len(tupla)):

    if tupla[i] == 9:
        cont9 += 1

    if tupla[i] == 3:
        if cont3 == 0:
            print(f'\nO primeiro valor 3 é encontrado na posição: {i + 1}')

    #if tupla[i] % 2 == 0 and tupla[i] != 0:


if cont3-1 == 0:
    print(f'\nNão foi encontrado nenhum valor 3.')
else:
    print(f'\nO primeiro valor 3 é encontrado na posição: {i + 1}')
print(f'Número de vezes em que o valor 9 foi encontrado: {cont9}')
