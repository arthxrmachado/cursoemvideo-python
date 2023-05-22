'''Faça um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:

- 1 para binário
- 2 para octal
- 3 para hexadecimal

ps.: Sem usar o conversor do próprio Python'''

num = int(input('Digte um número inteiro: '))

print('\n1 - Binário')
print('2 - Octal')
print('3 - Hexadecimal')
opcao = int(input('\nEscolha para que base deseja converter: '))

resposta = ''

print(f'\nNúmero inteiro: {num}')

if (opcao != 1 and opcao !=2 and opcao !=3):
    print('Opção inválida.')

elif (opcao == 1):

    while(num>=2):
        resposta += str(num%2)
        num = int(num/2)
    resposta += str(num)
    print(f'Número em binário: {resposta[::-1]}')

elif (opcao == 2):

    while(num>=8):
        resposta += str(num%8)
        num = int(num/8)
    resposta += str(num)
    print(f'Número em binário: {resposta[::-1]}')

else:

    while (num>=16):
        if(num%16 == 10):
            resposta += 'A'
        elif(num%16 == 11):
            resposta += 'B'
        elif(num%16 == 12):
            resposta += 'C'
        elif(num%16 == 13):
            resposta += 'D'
        elif(num%16 == 14):
            resposta += 'E'
        elif(num%16 == 15):
            resposta += 'F'
        else:
            resposta += str(num%16)
        num = int(num/16)
    if (num % 16 == 10):
        resposta += 'A'
    elif (num % 16 == 11):
        resposta += 'B'
    elif (num % 16 == 12):
        resposta += 'C'
    elif (num % 16 == 13):
        resposta += 'D'
    elif (num % 16 == 14):
        resposta += 'E'
    elif (num % 16 == 15):
        resposta += 'F'
    else:
        resposta += str(num)
    print(f'Número em hexadecimal: {resposta[::-1]}')