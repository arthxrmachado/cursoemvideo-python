''' Faça um programa que leia dos números inteiros e compare-os mostrando na tela uma das mensagens:

- O primeiro valor é maior;
- O segundo valor é maior;
- Os dois valores são iguais. '''

n1 = int(input('Digte um número inteiro: '))
n2 = int(input('Digte outro número inteiro: '))

if n1>n2:
    print('\nO primeiro valor digitado é o maior.')
elif n2>n1:
    print('\nO segundo valor digitado é o maior.')
else:
    print('\nOs dois valores são iguais.')