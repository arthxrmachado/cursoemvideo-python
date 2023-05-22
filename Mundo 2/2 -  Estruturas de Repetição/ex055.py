# Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior peso e o menor peso lidos.

maior = 0
menor = 0

for i in range (0, 5):
    peso = float(input("Digite seu peso: "))

    if menor == 0:
        menor = peso
    if peso>=maior:
        maior = peso
    elif peso<=menor:
        menor = peso

print(f'\nO maior peso digitado foi: {maior}\nO menor peso digitado foi: {menor}')