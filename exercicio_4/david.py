'''Trabalho feito por david, gabriel rech e gabriel sgorla'''

nota100 = 6
nota50 = 6
nota20 = 6
nota10 = 6
notas = 0

while True:

    saque = int(input("Digite quanto sacar: "))

    if saque // 100 >= 1 and nota100 > 0:
        notas = saque // 100
        saque = saque % 100
        nota100 -= notas
        print("A quantidade de notas de 100: ", notas)
    if saque // 50 >= 1 and nota50 > 0:
        notas = saque // 50
        saque = saque % 50
        nota50 -= notas
        print("A quantidade de notas de 50: ", notas)
    if saque // 20 >= 1 and nota20 > 0:
        notas = saque // 20
        saque = saque % 20
        nota20 -= notas
        print("A quantidade de notas de 20: ", notas)
    if saque // 10 >= 1 and nota10 > 0:
        notas = saque // 10
        saque = saque % 10
        nota10 -= notas
        print("A quantidade de notas de 10: ", notas)
    if nota100 == 0 and nota50 == 0 and nota20 == 0 and nota10 == 0:
        print("Saque nao disponivel!")
        break

print("Fim do programa")
