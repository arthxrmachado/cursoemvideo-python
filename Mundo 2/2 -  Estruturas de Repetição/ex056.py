''' Faça um programa que leia nome, idade e sexo de 4 pessoas. No final do programa mostre:

- A média de idade do grupo;
- Qual é o nome do homem mais velho;
- Quantas mulheres têm menos de 20 anos. '''

maior_idade = 0
media_idade = 0
cont_mulher = 0

for i in range (0, 2):
    nome = str(input('Digite o seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite o seu sexo (M/F): ')).upper()
    print('')

    if sexo == 'M':
        if idade>=maior_idade:
            maior_idade = idade
            maior_nome = nome
    else:
        if idade<20:
            cont_mulher += 1

    media_idade += idade

print(f'\nMédia de idade do grupo: {media_idade/2}')
print(f'Nome do homem mais velho: {maior_nome}')
print(f'Mulheres com menos de 20 anos: {cont_mulher}')