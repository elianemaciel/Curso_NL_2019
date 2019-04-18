#!/usr/bin/python
# -*- coding: utf-8 -*-
'''Gabriel Sgorla, Mateus, Pedro'''
from conta import Conta
from cliente import Cliente
from random import randint
from historico import Historico


listCli = []

def main():
    print("-----------------------------------")
    print("| 1 - Cadastrar Cliente e Conta   |")
    print("| 2 - Deposito                    |")
    print("| 3 - Saque                       |")
    print("| 4 - Extrato                     |")
    print("| 5 - Historicos                  |")
    print("| 0 - Sair                        |")
    print("-----------------------------------")
    opc = int(input("? >"))

    if opc == 1:
        nome = input("Nome: ")
        sobrenome = input("Sobrenome: ")
        cpf = input("CPF: ")
        salario = float(input("Digite seu salario: "))
        limite = salario * (50/100)
        saldo = float(input("Deposite um valor para abrir a conta: "))
        numero = randint(1000, 2000)
        cliente = Cliente(nome, sobrenome, cpf)
        conta = Conta(numero, cliente, saldo, limite)
        listCli.append(conta)
        print("Seja bem vindo, {} {}".format(conta.titular.nome, conta.titular.sobrenome))
        print("Numero da conta: {}".format(conta.numero))
        print("Seu limite é de: R${}".format(conta.limite))
        main()

    elif opc == 2:

        num = int(input("Digite o numero da conta: "))
        dep = float(input("Digite o valor a ser depositado: "))

        for i in range(len(listCli)):
            if num == listCli[i].numero:
                print("Nome: {} {}\nNumero da conta: {}".format(listCli[i].titular.nome, listCli[i].titular.sobrenome, listCli[i].numero))
                listCli[i].deposita(dep)

        main()

    elif opc == 3:

        num = int(input("Digite o numero da conta: "))
        saque = float(input("Digite o valor a ser sacado: "))

        for i in range(len(listCli)):
            if num == listCli[i].numero:
                print("Nome: {} {}\nNumero da conta: {}".format(listCli[i].titular.nome, listCli[i].titular.sobrenome, listCli[i].numero))
                listCli[i].saca(saque)

        main()

    elif opc == 4:

        num = int(input("Digite o numero da conta: "))
        for i in range(len(listCli)):
            if num == listCli[i].numero:
                print("Nome: {} {}\nNumero da conta: {}\nSaldo: {}\nLimite: {}\n".format(listCli[i].titular.nome, listCli[i].titular.sobrenome, listCli[i].numero, listCli[i].saldo, listCli[i].limite))
        main()

    elif opc == 5:

        num = int(input("Digite o numero da conta: "))
        for i in range(len(listCli)):
            if num == listCli[i].numero:
                for j in range(len(listCli[i].listaHist)):
                    listCli[i].listaHist[j].mostraHist()

        main()

    elif opc == 0:

        exit()

    else:

        print("Opção invalida")
        main()

main()
