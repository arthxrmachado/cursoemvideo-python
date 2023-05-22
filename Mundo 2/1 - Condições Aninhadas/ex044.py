''' Faça um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de
pagamento:

- À vista no dinheiro: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros'''

produto = float(input('Digite o valor do produto: '))

print('\n1 - À vista (Dinheiro ou Cheque)\n2 - À vista (Cartão)\n3 - Em até 2 vezes no Cartão\n4 - Mais de 3 vezes no cartão')

opcao = int(input('\nSelecione o método de pagamento: '))

if (opcao == 1):
    produto = produto - (produto*10/100)
    print(f'\nVocê recebeu 10% de desconto por pagar à vista.\nTotal do produto: {produto:.2f}')

elif (opcao == 2):
    produto = produto - (produto*5/100)
    print(f'\nVocê recebeu 5% de desconto por pagar à vista.\nTotal do produto: {produto:.2f}')

elif (opcao == 3):
    print(f'\nVocê dividiu o valor total do produto em 2 parcelas sem juros de {produto/2:.2f}.'
          f'\nTotal do produto: {produto:.2f}')

else:
    parcela = int(input('\nDigite o número de parcelas que deseja pagar: '))
    produto = produto + (produto*20/100)
    print(f'\nVocê dividiu o valor total do produto em {parcela} parcelas com juros. '
          f'Valores das parcelas: {produto/parcela:.2f}'
          f'\nTotal do produto: {produto:.2f}')