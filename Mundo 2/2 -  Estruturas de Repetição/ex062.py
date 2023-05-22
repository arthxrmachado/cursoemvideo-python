''' Faça um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa
progressão. No final, pergunte ao usuário se ele quer colocar mais alguns termos, o programa termina quando o usuário
disser que quer mostrar 0 termos.'''

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite uma razão: '))

opcao = 1
contador = 0
delimitador = 10
total = 0

while opcao != 0:

    while contador < delimitador:

        print(termo)
        termo += razao

        #variável utilizada apenas para mostrar quantos termos foram apresentados, ao final do programa
        total += 1

        contador += 1

    opcao = int(input('\nDigite a quantidade de termos a mais que você deseja ver: '))
    print('')

    contador = 0
    delimitador = opcao

print(f'Progressão finalizada com {total} termos apresentados.')