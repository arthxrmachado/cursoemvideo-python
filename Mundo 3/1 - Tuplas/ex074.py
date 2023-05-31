''' Faça um programa que gere cinco números aleatórios e coloquem-os em uma tupla. Depois disso, mostre a listagem de
números gerados e também indique o menor e o maior valor que estão na tupla. '''

from random import randint

tupla = (randint(1,100), randint(1,100), randint(1,100), randint(1,100), randint(1,100))
menor = maior = 0

print(tupla)

for i in range (0, len(tupla)):
    if i == 0:
        menor = tupla[i]
        maior = tupla[i]

    else:
        if tupla[i]>maior:
            maior = tupla[i]

        elif tupla[i]<menor:
            menor = tupla[i]

#print(f'Maior número: {max(tupla)}\nMenor número: {min(tupla)}') <- sem usar estrutura de repetição
print(f'Maior número: {maior}\nMenor número: {menor}')
