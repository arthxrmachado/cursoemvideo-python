''' Faça um tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol, na ordem de
colocação.

Depois mostre:

- Apenas os cinco primeiros colocados;
- Os últimos quatro colocados da tabela;
- Uma lista com todos os times em ordem alfabética;
- Em que posição da tabela está o time do Botafogo.

ps.: usarei a tabela do Brasileirão 2022.'''

tabela = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico-PR', 'Atlético-MG',
          'Fortaleza', 'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá',
          'Ceará', 'Atlético-GO', 'Avaí', 'Juventude')

print('-'*50)

print(f'Cinco primeiros:\n\n{tabela[0:5]}')
print('-'*50)

print(f'Quatro últimos:\n\n{tabela[16:20]}')#ou tabela[-4:]
print('-'*50)

print(f'Ordem alfabética:\n\n{sorted(tabela)}')
print('-'*50)

print(f'\nO time do Botafogo terminou o campeonato na {tabela.index("Botafogo")+1}ª colocação.\n')
print('-'*50)

#for i in range (0, len(tabela)):
    #if tabela[i] == 'Botafogo':
        #print(f'\nO time do Botafogo terminou o campeonato na {i+1}ª colocação.\n')