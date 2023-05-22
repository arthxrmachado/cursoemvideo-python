''' Faça um programa que leia uma frase e verifique se ela é um palíndromo, desconsiderando os espaços e acentos.

Exemplos de palíndromos:

- APOS A SOPA;
- A SACADA DA CASA;
- A TORRE DA DERROTA;
- O LOBO AMA BOLO;
- ANOTARAM A DATA DA MARATONA.

ps.: usando estruturas de repetição'''

frase = str(input('Digite uma frase: ')).strip().upper()
separar = frase.split()
juntar = ''.join(separar)
inverso = ''

for i in range (len(juntar)-1, -1, -1):
    inverso += juntar[i]

print(f'\nFrase digitada: {juntar}')
print(f'Frase invertida: {inverso}')

if inverso == juntar:
    print(f'\nA frase digitada é um palíndromo.')
else:
    print(f'\nA frase digitada não é um palíndromo.')