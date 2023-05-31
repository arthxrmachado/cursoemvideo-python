''' Faça um programa que leia vários números e coloque-os numa lista. Depois disso, mostre:

- Quantos números foram digitados;
- A lista de valores, ordenados de forma decrescente;
- Se o valor 5 foi digitado e está ou não na lista. '''

valores = list()
#valores = list[]

while True:
    valores.append(int(input('Digite um valor: ')))

    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]

    if opcao == 'N':
        break

print(f'\nForam digitados {len(valores)} valores.')

valores.sort(reverse=True)
print(f'Valores digitados em ordem: {valores}')

if 5 in valores:
    print(f'O valor 5 existe na lista.')
else:
    print(f'Não existe o valor 5 na lista.')