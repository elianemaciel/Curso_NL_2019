# Faça um Programa que peça os 3 lados de um triângulo.
# O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero,
# isósceles ou escaleno.
# Dicas: Três lados formam um triângulo quando a soma de quaisquer dois
# lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;

lado1 = float(input('Digite a primeira medida: '))
lado2 = float(input('Digite a segunda medida: '))
lado3 = float(input('Digite a terceira medida: '))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    if lado1 == lado2 == lado3:
        print('As medidas digitadas formam um triângulo EQUILÁTERO!')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('As retas digitadas podem formar um triângulo ISÓSCELES!')
    else:
        print('As retas digitadas formam um triângulo ESCALENO!')
else:
    print('As retas digitadas não podem formar um triângulo!')
