''' Crie um programa que leia o nome completo de uma pessoa e mostre:

- O nome com todas as letras maiúsculas e minúsculas;
- Quantas letras o nome tem (desconsiderando os espaços);
- Quantas letra tem o primeiro nome. '''

nome = str(input('Digite seu nome completo: ')).strip()

print(f'\nSeu nome completo: {nome}')
print(f'Seu nome completo em maiúsculo: {nome.upper()}')
print(f'Seu nome completo em minúsculo: {nome.lower()}')

print(f'\nSeu nome tem ao todo {len(nome) - nome.count(" ")} letras.')

#print (f'\nSeu primeiro nome tem ao todo {nome.find(" ")} letras.')

separa = nome.split()
print(f'Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras.')