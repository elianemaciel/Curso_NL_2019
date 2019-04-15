a = input("Lado A: ")
b = input("Lado B: ")
c = input("Lado C: ")

if a == b and b == c:
    print("Triângulo equilátero!")
elif a == b or b == c:
    print("Triângulo isóscelos!")
elif a != b and b != c:
    print ("Triângulo escaleno!")
else:
    print("Não é um triângulo!")