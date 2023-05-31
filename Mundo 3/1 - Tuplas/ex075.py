''' Faça um programa que leia quatro valores pelo teclado e armazene-os em uma tupla. No final, mostre:

- Quantas vezes apareceu o valor 9;
- Em que posição foi digitado o primeiro valor 3;
- Quais foram os números pares. '''

tupla = (int(input('Digite um número inteiro: ')), int(input('Digite um número inteiro: ')), int(input('Digite um número inteiro: ')),
         int(input('Digite um número inteiro: ')))
contPar = 0

print(f'\nO valor 9 foi encontrado {tupla.count(9)} vezes.')

if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3)+1}ª posição.')
else:
    print(f'O valor 3 não foi encontrado.')

print(f'Os valores pares digitados foram: ', end='')
for i in tupla:
    if (i != 0):
        if (i%2 == 0):
            print(i, end=' ')

print('')