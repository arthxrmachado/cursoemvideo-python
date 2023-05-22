''' Faça um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com
a média atingida:

- Média abaixo de 4.0: REPROVADO;
- Média entre 4.0 e 5.9: RECUPERAÇÃO;
- Média 6.0 ou superior: APROVADO. '''

av1 = float(input('Digite a primeira nota: '))
av2 = float(input('Digite a segunda nota: '))

media = (av1+av2)/2

if media < 4.0:
    print(f'\nMédia do aluno: {media}\nEste aluno está REPROVADO.')
elif media >= 4.0 and media < 6.0:
    print(f'\nMédia do aluno: {media}\nEste aluno está em RECUPERAÇÃO.')
else:
    print(f'\nMédia do aluno: {media}\nEste aluno está APROVADO.')