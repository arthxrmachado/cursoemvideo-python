''' Faça um programa que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a
tabela abaixo:

- Abaixo de 18.5: abaixo do peso;
- Entre 18.5 e 25: peso ideal;
- 25 até 30: sobrepeso;
- 30 até 40: obesidade;
- Acima de 40: obesidade mórbida.'''

peso = int(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

if altura.is_integer():
    altura = altura/100

imc = peso/(altura*altura)

print(f'\nSeu IMC é: {imc:.2f}')

if imc < 18.5:
    print('\nVocê está abaixo do peso ideal.')

elif imc <= 25:
    print('\nVocê está no peso ideal.')

elif imc <= 30:
    print('\nVocê está um pouco acima do peso ideal.')

elif imc <= 40:
    print('\nVocê está obesa(o).')

else:
    print('\nVocê está com obesidade mórbida.')