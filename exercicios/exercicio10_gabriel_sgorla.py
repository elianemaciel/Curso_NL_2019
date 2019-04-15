lado1 = float(input(print("Digite o primeiro lado: ")))
lado2 = float(input(print("Digite o segundo lado: ")))
lado3 = float(input(print("Digite o terceiro lado: ")))

if (lado1 + lado2) > lado3 and (lado1 + lado3) > lado2 and (lado3 + lado2) > lado1:
    if lado1 == lado2 and lado2 == lado3:
        print("Triangulo Equilatero")
    elif lado1 == lado2 or lado1 == lado3 or lado3 == lado2:
        print("Triangulo Isosceles")
    else:
       print("Triangulo Escaleno")
else:
    print("Nao eh triangulo")
