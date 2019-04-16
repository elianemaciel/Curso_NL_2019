nota1 = int(input("Insira um número: "))
nota2 = int(input("Insira outro número: "))

media = (nota1+nota2)/2

if media >=7 and media <10:
    print("Aprovado")
elif media <7:
    print("Reprovado")
elif media == 10:
    print("Aprovado com Distinção")
