''' Faça um programa onde o usuário digita uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar
se a expressão passada está com os parenteses abertos e fechados na ordem correta. '''

expressao = str(input('Digite sua expressão: '))
pilha = list()

for s in expressao:
    if s == '(':
        pilha.append('(')

    elif s == ')':
        if len(pilha) > 0:
            pilha.pop()

        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print(f'\nSua expressão é válida.')

else:
    print(f'\nSua expressão NÃO é válida.')