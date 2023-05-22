# Faça um programa que mostre na tela todos os números pares que estão no intervalo de 1 a 50.

''' Faz mais iterações, ocupa mais da memória

for i in range (1, 51):
    if i%2 == 0:
        print(i, end=' ') '''

# Melhor jeito de se fazer, usando menos memória

for i in range (2, 51, 2):
    print(i, end=' ')

print('\n\nEsses foram todos os números pares no intervalo de 1 a 50.')