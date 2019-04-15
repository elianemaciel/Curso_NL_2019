"""Faça um programa que leia dois valores x e y.
O programa deve trocar os valores lidos, de forma que, ao final, x
contenha o valor que foi inicialmente atribuído em y, e y contenha
o valor que foi inicialmente atribuído a x. Imprima os valores de x e y logo após a leitura,
e depois imprima novamente após a troca."""

x = int(input("Digite valor x: "))
y = int(input("Digite valor y: "))
aux = 0

aux = x
x = y
y = aux

print("o novo valor de x: ",x)
print("o novo valor de y: ",y)
