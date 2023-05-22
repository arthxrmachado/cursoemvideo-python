''' Faça um programa que leia dois valores e mostre o menu seguinte na tela:

[1] Soma
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair

Seu programa deverá realizar a operação solicitada em cada caso. '''

opcao = '0'

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

while opcao != '5':

    print(f'\n[1] Soma\n[2] Multiplicar\n[3] Maior número\n[4] Editar números\n[5] Sair')
    opcao = str(input('\nEscolha uma opção: '))

    if opcao == '1':
        print(f'\n{n1} + {n2} = {n1+n2}')

    elif opcao == '2':
        print(f'\n{n1} x {n2} = {n1*n2}')

    elif opcao == '3':

        if n1 == n2:
            print(f'\nOs dois números são iguais.')
            
        if n1 > n2:
            print(f'\nO número {n1} é maior que {n2}.')

        else:
            print(f'\nO número {n2} é maior que {n1}.')

    elif opcao == '4':
        n1 = int(input('\nDigite um número: '))
        n2 = int(input('Digite outro número: '))

    else:
        if opcao != '5':
            print(f'\nOpção inválida! Tente novamente.')
        else:
            print(f'\nFim do programa.')