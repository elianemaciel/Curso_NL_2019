nota1 = float(input(print("Digite a primeira nota: ")))
nota2 = float(input(print("Digite a segunda nota: ")))

media = (nota1 + nota2)/2

if media >= 7 and media < 10:
    print("APROVADO!")
elif media < 7:
    print("REPROVADO!")
elif media == 10:
    print("APROVADO COM DISTINCAO!")
