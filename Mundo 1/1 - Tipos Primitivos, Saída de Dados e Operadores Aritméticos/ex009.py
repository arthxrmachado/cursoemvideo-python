''' Faça um programa que leia a largura e a altura de uma parede em metros. Calcule sua área e a quantidade de tinta
necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m². '''

largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))

area = largura*altura

print(f'Para pintar uma parede de área {area}m² são necessários {area/2:.2f} litros de tinta.')
