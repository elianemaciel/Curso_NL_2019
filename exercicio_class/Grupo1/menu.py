#!/usr/bin/python
# -*- coding: utf-8 -*-
'''Gabriel Sgorla, Mateus, Pedro'''
from conta import Conta
from cliente import Cliente

listCli = []

def main():
    print("-----------------------------------")
    print("| 1 - Cadastrar Cliente e Conta   |")
    print("| 2 - Deposito                    |")
    print("| 3 - Saque                       |")
    print("| 4 - Extrato                     |")
    print("| 0 - Sair                        |")
    print("-----------------------------------")
    opc = int(input("? >"))

    if opc == 1:
        nome = input("Nome: ")
        sobrenome = input("Sobrenome: ")
        cpf = input("CPF: ")
        cliente = Cliente(nome, sobrenome, cpf)
        listCli.append(cliente)
        print(listCli)
        main()
main()
