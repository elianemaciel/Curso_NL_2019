''''Exercicio feito por David,Gabriel Rech e Gabriel Sgorla'''

lista_fun []
dados ={}
for x in range(5):
    def adic(dados):
        nome = input("Digite o nome do Funcionário:")
        loja = input("Digite a loja do Funcionário:")
        vendas = input("Digite o valor de vendas:")
        dados = {"Nome:"nome,"Loja:"Loja,"Vendas:"vendas}

        return dados
    lista.append(func(dados))
print(lista)
print("-----------------")

def maximo(lista):
    return max(lista, key=(lambda x: x['vendas'])) 

maximo = maximo(lista)
print(maximo["nome"])

def order_sal(lista):
    sorted(lista, key=(lambda x x:["Vendas"]),reverse = True)
    x = [i["nome"] for i in y]
    return x

ordem = order_sal(lista)
print(ordem)

def maxloja(lista):
    l= int(input("Informe qual loja você deseja buscar"))
    lista2 = list(filter(lambda x: x["loja"]==l,lista))
