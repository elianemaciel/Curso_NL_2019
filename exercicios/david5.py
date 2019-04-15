#Faça um Programa que peça dois números e imprima o maior deles.​
n1 = int(input("Digite um valor: "))
n2 = int(input("Digite um segundo valor: "))

if n1 > n2:
    print("O maior numero e: ",n1)

elif n2 > n1:
    print("O maior numero e: ",n2)

elif n1 ==n2:
    print("Numeros Iguais")
