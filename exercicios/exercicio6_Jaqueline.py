# Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

valor = int(input('Digite um valor: '))

if valor > 0:
    print('Valor digitado é positivo.')
elif valor < 0:
    print('Valor digitado é negativo.')
else:
    print('Valor digitado é zero.')
    
