a = float(input(print("Digite o primeiro lado: ")))
b = float(input(print("Digite o segundo lado: ")))
c = float(input(print("Digite o terceiro lado: ")))

if (a + b) > c and (a + c) > b and (c + b) > a:
    if a == b and b == c:
        print("Triangulo Equilatero")
    elif a == b or a == c or c == b:
        print("Triangulo Isosceles")
    else:
       print("Triangulo Escaleno")
else:
    print("Nao eh triangulo")
