# Caixa Eletrônico
# Desenvolva um programa que simule a entrega de notas quando um cliente
# efetuar um saque em um caixa eletrônico. Os requisitos básicos são os seguintes:​

# - Entregar o menor número de notas;​
# - É possível sacar o valor solicitado com as notas disponíveis;​
# - Saldo do cliente infinito;​
# - Quantidade de notas infinito (pode-se colocar um valor finito de
# cédulas para aumentar a dificuldade do problema);​
# - Notas disponíveis de R$ 100,00; R$ 50,00; R$ 20,00 e R$ 10,00​

## Exemplos:​
# - Valor do Saque: R$ 30,00 – Resultado Esperado:
# Entregar 1 nota de R$20,00 e 1 nota de R$ 10,00.​
# - Valor do Saque: R$ 80,00 – Resultado Esperado:
# Entregar 1 nota de R$50,00 1 nota de R$ 20,00 e 1 nota de R$ 10,00. ​​

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
