# test

def sacar(valor):
    
    while valor != 0:

        if valor >= 100:
            print("nota de 100.00")
            valor = valor - 100
            continue

        if valor >= 50:
            print("nota de 50.00")
            valor = valor - 50
            continue

        if valor >= 20:
            print("nota de 20.00")
            valor = valor - 20
            continue

        if valor >= 10:
            print("nota de 10.00")
            valor = valor - 10
            continue

sacar(700)