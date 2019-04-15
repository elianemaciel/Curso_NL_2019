a = 11
b = 14
c = 14

if a == b and b == c:
    print("Triângulo equilátero!")
elif a == b or b == c:
    print("Triângulo isóscelos!")
elif a != b and b != c:
    print ("Triângulo escaleno!")
else:
    print("Não é um triângulo!")