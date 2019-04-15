# Faça um programa que leia dois valores x e y. O programa deve trocar os
# valores lidos, de forma que, ao final, x contenha o valor que foi
# inicialmente atribuído em y, e y contenha o valor que foi inicialmente
# atribuído a x. Imprima os valores de x e y logo após a leitura, e depois
# imprima novamente após a troca.

x = int(input('Digite um valor inteiro: '))
y = int(input('Digite um segundo valor inteiro: '))

print('Valor atribuído a x: {}, valor atribuído a y: {}.'.format(x, y))

aux = x
x = y
y = aux

print('Valor de x passou a ser: {}, de y passou a ser: {}.'.format(x, y))
