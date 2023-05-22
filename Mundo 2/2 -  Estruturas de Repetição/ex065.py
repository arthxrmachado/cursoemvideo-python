''' Faça um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
valores e qual foi o maior e menor valores lidos. O programa deve perguntar ao usuário se ele quer continuar ou não a
digitar valores. '''

opcao = 'S'
cont = total = maior = 0

while opcao == 'S':

    n = int(input('Digite  um número inteiro: '))

    #se o programa estiver rodando pela primeira vez, a váriavel 'menor' receberá o valor de 'n', afinal se o usuário digitou
    #apenas um número, esse é o maior e o menor número digitado'''
    if cont == 0:
        menor = n

    if n>maior:
        maior = n

    elif n<menor:
        menor = n

    #atualizando a váriavel 'total' com cada valor digitado, assim no final será possível efetuar a média
    total += n

    #coloquei um contador para contar quantos valores foram digitados
    cont += 1

    opcao = str(input('Deseja continuar? [S/N]: ')).upper().strip()
    print('')

print(f'Valores digitados: {cont}\nMédia total: {total/cont:.2f}\nMaior valor: {maior}\nMenor valor: {menor}')