nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))

if (nota1 + nota2)/2 == 10:
    print("APROVADO com Distinção!")
elif (nota1 + nota2)/2 >= 7:
    print ("APROVADO!")
elif (nota1 + nota2)/2 < 7:
    print("REPROVADO!")
else:
    print ("REPROVADO")

