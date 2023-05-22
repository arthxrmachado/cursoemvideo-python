''' Faça um programa que dado o salário de um funcionário calcule o valor do seu aumento.

Salários superiores a R$ 1250,00 calcule um aumento de 10%.
Inferiores ou iguais o aumento é de 15%.'''

salario = float(input('Digite o salário do funcionário: '))

if salario>1250.00:
    aumento = 10/100*salario
    print(f'\nO funcionário receberá um aumento de R$ {aumento:.2f}\nSeu novo salário será de: {aumento+salario:.2f}')

else:
    aumento = 15/100*salario
    print(f'O funcionário receberá um aumento de R$ {aumento:.2f}\nSeu novo salário será de: {aumento+salario:.2f}')