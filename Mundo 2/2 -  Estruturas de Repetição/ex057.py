''' Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a
digitação novamente até ter um valor correto. '''

opcao = 'S'
masculino = feminino = 0

while opcao != 'N':

    sexo = str(input('Digite seu sexo (M/F): ')).upper()

    if sexo == 'M':
        masculino += 1

    elif sexo == 'F':
        feminino += 1

    else:
        print('Opção inválida! Tente novamente.')

    opcao = str(input('Deseja continuar? [S/N]: ')).upper()

print (f'\nForam digitados {masculino} pessoas do sexo masculino e {feminino} pessoas do sexo feminino.')