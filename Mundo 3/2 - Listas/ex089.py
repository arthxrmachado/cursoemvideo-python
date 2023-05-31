''' Faça um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre
um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente. '''

temp = []
notas = []

while True:
    temp.append(str(input('Digite o nome do aluno: ')))
    temp.append(float(input('Digite a primeira nota do aluno: ')))
    temp.append(float(input('Digite a segunda nota do aluno: ')))

    notas.append(temp[:])
    temp.clear()

    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]

    if opcao == 'N':
        break

    print('')

print('=' * 25)
print(f'{"No.":<5}{"Nome:":<15}{"Média":<5}')
print('')
for i, j in enumerate(notas):
    print(f'{i+1:<5}{j[0]:<15}{(j[1]+j[2])/2:<5}')
print('=' * 25)

while True:
    opcao = int(input('\nDigite o número do aluno que deseja ver as notas (999 interrompe): '))

    if opcao == 999:
        break

    else:
        for i, j in enumerate(notas):
            if opcao-1 == i:
                print(f'\nAluno: {j[0]}\nAV1: {j[1]} / AV2: {j[2]}\nMédia: {(j[1]+j[2])/2}')