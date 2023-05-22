''' Faça um programa que pergunte a quantidade de quilômetros percorridos por um carro alugado e a quantidade de dias
pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por quilôme-
tro rodado. '''

km = float(input('Digite a quantidade de quilômetros percorridos: '))
dias = int(input('Digite a quantidade de dias o carro esteve alugado: '))

print(f'Quilômetros rodados: {km}\nDias alugado: {dias}\nPreço total: R$ {km*0.15+dias*60.00:.2f}')
