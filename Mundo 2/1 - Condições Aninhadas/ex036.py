''' Faça um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa irá perguntar o valor da
casa, o salário do comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.'''

casa = float(input('Digite o valor da casa a ser comprada: '))
salario = float(input('Digite o salário do comprador: '))
anos = int(input('Digte em quantos anos será pago: '))

parcela = (casa/anos)/12

if (salario*30/100 >= parcela):
    print(f'\nEmpréstimo efetuado!\n')
else:
    print(f'\nEmpréstimo negado!\n')

print(f'Valor total da casa: {casa:.2f}')
print(f'Salário do comprador: {salario:.2f}')
print(f'Quantidade de anos em que será pago: {anos}')
print(f'\nValor total da parcela: {parcela:.2f}')
print(f'30% do salário do comprador: {salario*30/100:.2f}')