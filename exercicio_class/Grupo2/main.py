from conta import Conta
from cliente import Cliente

contaCriada = None
print("DIGITE 1 PARA CADASTRAR CLIENTE")
print("DIGITE 2 PARA SACAR")
print("DIGITE 3 PARA DEPOSITAR")
print("DIGITE 4 PARA EXTRATO")
entrada = int(input("ESCOLHA A FUNÇÃO: "))
if entrada == 1:
    a= input("Nome:")
    b= input("Sobrenome:")
    c= input("CPF:")
    d= Cliente(nome=a, sobrenome=b,cpf=c)
    s= input("Número da conta:")
    x= input("Saldo inicial da conta:")
    y= input("Limite da conta:")
    contaCriada = Conta(numero=s, titular=d, saldo=x, limite=y)
if entrada == 2:
    valorSaque = int(input('valor do saque: '))
    contaCriada.saca(valorSaque)
