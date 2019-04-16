# Obs: Dsenvolvido por Jaqueline e Pedro

notas = [100, 50, 20, 10]
restoSaque, notasCem, notas50, notas20, notas10 = 0, 0, 0, 0, 0
while True:
    saque = int(input('Digite valor do saque: '))
    notasCem = saque // 100
    restoSaque = saque % 100
    notas50 = restoSaque // 50
    restoSaque = restoSaque % 50
    notas20 = restoSaque // 20
    restoSaque = restoSaque % 20
    notas10 = restoSaque // 10

    if notasCem > 0:
        print('Notas de 100 = {}'.format(notasCem))
    if notas50 > 0:
        print('Notas de 50 = {}'.format(notas50))
    if notas20 > 0:
        print('Notas de 20 = {}'.format(notas20))
    if notas10 > 0:
        print('Notas de 10 = {}'.format(notas10))

    if saque == 0:
        print('Saque indisponível')
        break
