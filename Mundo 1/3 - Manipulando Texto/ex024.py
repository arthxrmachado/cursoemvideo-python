# Faça um programa que leia o nome de uma cidade e diga se ela começa com a palavra "Santo" ou não.

cidade = str(input('Digite o nome de uma cidade: ')).strip()

print(cidade[:5].lower() == 'santo')