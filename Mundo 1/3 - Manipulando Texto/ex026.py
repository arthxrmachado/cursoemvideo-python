''' Faça um programa que leia uma frase e mostre:

- Quantas vezes aparece a letra "A";
- Em que posição ela aparece pela primeira vez;
- Em que posição ela aparece pela última vez. '''

frase = str(input('Digite uma frase: ')).strip()

print(f'\nA letra "A" aparece {frase.lower().count("a")} vezes na frase.')
print(f'A primeira vez que a letra "A" aparece na frase é na posição: {frase.lower().find("a")}')
print(f'A última vez que a letra "A" aparece na frase é na posição: {frase.lower().rfind("a")}')