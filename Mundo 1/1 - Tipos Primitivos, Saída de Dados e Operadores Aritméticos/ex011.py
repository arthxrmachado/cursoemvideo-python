# Faça um programa que leia o salário de um funcionário e mostre seu novo salário, com um aumento de 15%.

salario = float(input('Digite o salário do funcionário: '))

print (f'O salário desse funcionário passou de R${salario:.2f} para R${salario+salario*15/100:.2f}.')
