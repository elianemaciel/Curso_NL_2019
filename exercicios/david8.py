"""Faça um programa para a leitura de duas notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez."""

nota1 = float(input("Digite nota 1: "))
nota2 = float(input("Digite nota 2: "))

soma = nota1 + nota2
media = soma /2

if media>=7 and media<10:
    print("Aprovado,Media = ",media)
elif media<7:
    print("Reprovado,Media = ",media)
elif media ==10:
    print("Aprovado com Distincao,Media = ",media)
