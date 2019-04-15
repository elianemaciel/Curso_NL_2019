"""Faça um Programa que peça os 3 lados de um triângulo.
O programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno."""


lado1 = float(input("Digite lado 1: "))
lado2 = float(input("Digite lado 2: "))
lado3 = float(input("Digite lado 3: "))

if (lado1 + lado2) > lado3 and (lado1 + lado3) > lado2 and (lado3 + lado2) > lado1:
    if lado1 == lado2 and lado2 == lado3:
        print("Triangulo Equilatero")
    elif lado1 == lado2 or lado1 == lado3 or lado3 == lado2:
        print("Triangulo Isosceles")
    else:
       print("Triangulo Escaleno")
else:
    print("Nao eh triangulo")
