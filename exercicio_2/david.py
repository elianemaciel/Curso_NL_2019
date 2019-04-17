'''Exercicio feito por David,Gabriel Rech e Gabriel Sgorla '''
lista =[]
dados ={}
for x in range(5):
    def func(dados):
        nome = input("Digite o nome do Funcionario: ")
        loja = int(input("Digite a loja do Funcionario: "))
        vendas = float(input("Digite o valor de vendas:  "))
        dados={"Nome":nome,"Loja":loja,"Vendas":vendas}

        return dados
    lista.append(func(dados))
print(lista)
print("---------------")

def maximo(lista):
    return max(lista, key=(lambda x : x["Vendas"]))

maximo = maximo(lista)
print(maximo["Nome"])

'''faça uma função que liste todos os
 vendedores ordenados pelo valor vendido, do maior para o menor.'''

def order(lista):
    y= sorted(lista, key=(lambda x : x["Vendas"]),reverse=True)
    x= [i["Nome"] for i in y]
    return x

ordem = order(lista)
print(ordem)

def maxloja(lista):
    l = int(input("Informe qual loja: "))
    lista2 =list(filter(lambda x: x["Loja"]==l,lista))

    return max(lista2, key=(lambda x : x["Vendas"]))

melhorvendedor = maxloja(lista)
print(melhorvendedor["Nome"])
