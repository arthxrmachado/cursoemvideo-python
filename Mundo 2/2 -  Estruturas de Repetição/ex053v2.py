''' Faça um programa que leia uma frase e verifique se ela é um palíndromo, desconsiderando os espaços e acentos.

Exemplos de palíndromos:

- APOS A SOPA;
- A SACADA DA CASA;
- A TORRE DA DERROTA;
- O LOBO AMA O BOLO;
- ANOTARAM A DATA DA MARATONA.

ps.: sem usar estruturas de repetição'''

frase = str(input('Digite uma frase: ')).strip().upper()
separar = frase.split()
juntar = ''.join(separar)
inverso = juntar[::-1]

print(f'\nFrase digitada: {juntar}')
print(f'Frase invertida: {inverso}')

if inverso == juntar:
    print(f'\nA frase digitada é um palíndromo.')
else:
    print(f'\nA frase digitada não é um palíndromo.')