a = 14
b = 14
c = 8

if a == b and b == c:
    print("Triângulo equilátero!")
elif a == b and a == c and b == c:
    print("Triângulo isóscelos!")
elif a != b and b != c:
    print ("Triângulo escaleno!")
else:
    print("Não é um triângulo!")