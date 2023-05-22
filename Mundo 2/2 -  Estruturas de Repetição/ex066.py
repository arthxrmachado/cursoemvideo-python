''' Faça um programa que leia vários números inteiros. O programa só irá parar quando o usuário digitar o valor 999, que
é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando a
condição de parada). '''

n = cont = soma = 0

while True:
    n = int(input('Digite um número inteiro: '))

    if n == 999:
        break

    soma += n
    cont += 1

print (f'\nNúmero digitados: {cont}\nSoma total: {soma}')