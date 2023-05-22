''' Faça um programa que leia a idade e sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se
o usuário quer ou não continuar. No final, mostre:

a) quantas pessoas tem mais de 18 anos.
b) quantos homens foram cadastrados.
c) quantas mulheres tem menos de 20 anos. '''

maioridade = homens = mulheres = 0

while True:
    idade = int(input('Digite sua idade: '))

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]

    if idade >= 18:
        maioridade += 1

    if sexo == 'M':
        homens += 1

    if sexo == 'F' and idade < 20:
        mulheres += 1

    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('\nDeseja continuar? [S/N]: ')).strip().upper()[0]

    print('')

    if escolha == 'N':
        break

print(f'Pessoas com mais de 18 anos: {maioridade}'
      f'\nHomens cadastrados: {homens}'
      f'\nMulheres com menos de 20 anos: {mulheres}')