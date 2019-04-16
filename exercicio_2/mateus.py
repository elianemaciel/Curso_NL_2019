vendedores = [
        {"name": "Joca",    "store": 1, "value": 1200.00},
        {"name": "Arlindo", "store": 2, "value": 3000.00},
        {"name": "Arispio", "store": 3, "value": 1500.00},
        {"name": "Carlão",  "store": 1, "value": 2000.00}
]

maiorVendedor = max(vendedores, key=(lambda x: x['value']))
ascValorVendas = sorted(vendedores, key=(lambda x: x['value']))
descValorVendas = ascValorVendas.reverse()

def bestSeller():
    print("Melhor vendedor: {}\nLoja: {}\nTotal Vendido: {}".format(maiorVendedor['name'], maiorVendedor['store'], maiorVendedor['value']))

def ascSeller():
    ascNames = [ascValorVendas[i]["name"] for i in range(len(ascValorVendas))]
    print(ascNames)

def descSeller():
    descNames = [descValorVendas[i]["name"] for i in range(len(descValorVendas))]
    print(descNames)

bestSeller()
