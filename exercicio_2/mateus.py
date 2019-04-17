vendedores = [
        {"name": "Joca",    "store": 1, "value": 1200.00},
        {"name": "Arlindo", "store": 2, "value": 3000.00},
        {"name": "Arispio", "store": 3, "value": 1500.00},
        {"name": "Carlão",  "store": 1, "value": 2000.00},
		{"name": "Maicão",  "store": 3, "value": 3000.90}
]

# Funcão para retornar melhor funcionário, recebe com parametro uma lista
def bestSaller(vendedores):
	melhorVendedor = max(vendedores, key=(lambda x: x['value']))
	return melhorVendedor['name'], melhorVendedor['store'], melhorVendedor['value']

# Ordena em ordem ascendente pelo valor de vendas
def ascSaller():
	ascValorVendas = sorted(vendedores, key=(lambda x: x['value']))
	print("Vendedores com menor venda:")
	for i in ascValorVendas:
		print("Vendedor: {}\nVendeu: {}\n---------".format(i['name'],i['value']))
	
# Ordena em ordem descrescente pelo valor de vendas
def descSaller():
	descValorVendas = sorted(vendedores, key=(lambda x: x['value']), reverse = True)
	print("Vendedores com maior venda:")
	for i in descValorVendas:
		print("Vendedor: {}\nVendeu: {}\n---------".format(i['name'],i['value']))

# Melhor vendedor em uma loja especifica
def bestSallerStore():
	store = int(input("Loja: "))
	melhorVendedor = list(filter(lambda x: x['store'] == store, vendedores))
	return bestSaller(melhorVendedor)

print("----------------------------------------------------------------")
print("Melhor de todas as lojas: {}".format(bestSaller(vendedores)[0]))
print("Loja: {}".format(bestSaller(vendedores)[1]))
print("Vendido: {}".format(bestSaller(vendedores)[2]))
print("----------------------------------------------------------------")
