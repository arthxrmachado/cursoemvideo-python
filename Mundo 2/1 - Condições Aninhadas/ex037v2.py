'''Faça um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:

- 1 para binário
- 2 para octal
- 3 para hexadecimal

ps.: Usando o conversor do próprio Python.'''

num = int(input('Digte um número inteiro: '))

print('\n1 - Binário')
print('2 - Octal')
print('3 - Hexadecimal')
opcao = int(input('\nEscolha para que base deseja converter: '))

print(f'\nNúmero inteiro: {num}')

if (opcao != 1 and opcao !=2 and opcao !=3):
    print('Opção inválida.')

elif (opcao == 1):
    print(f'Número em binário: {bin(num)[2:]}')

elif (opcao == 2):
    print(f'Número em binário: {oct(num)[2:]}')

else:
    print(f'Número em hexadecimal: {hex(num)[2:]}')