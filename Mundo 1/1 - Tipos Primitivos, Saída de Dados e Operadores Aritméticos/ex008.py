# Faça um programa que leia quanto dinheiro uma pessoa tem na carteira (em reais) e mostre por quantos doláres ela pode trocar.

# US$ 1,00 = R$ 5,19

n1 = float(input('Digite seu saldo: '))

print (f'Essa pessoa pode trocar seus R${n1} por US${n1/5.19:.2f}')
