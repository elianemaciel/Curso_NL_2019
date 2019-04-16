# Desenvolvido por Jaqueline e Pedro

vendedores = [{'Nome': "André", 'Loja':2, 'VendasMes': 2000},
              {'Nome': "Maria", 'Loja':1, 'VendasMes': 4000},
              {'Nome': "Lucas", 'Loja':2, 'VendasMes': 3500},
              {'Nome': "Pedro", 'Loja':2, 'VendasMes': 2250},
              {'Nome': "Carla", 'Loja':1, 'VendasMes': 1700}]

def maiorVendas(vendedores):
    nomeVendedor = (max(vendedores, key=(lambda x: x['VendasMes'])))
    return nomeVendedor['Nome']

print('Vendedor com maior número de vendas: {}'.format(maiorVendas(vendedores)))

def maiorMenor():
    ordemValor = sorted(vendedores, key = (lambda x: x['VendasMes']), reverse = True)
    lista = [nome["Nome"] for nome in ordemValor]
    return lista

print('Vendedores com valor vendido do maior para menor: {}'.format(maiorMenor()))

def melhorVendedor():
    loja = int(input('Loja: '))
    lista = list(filter(lambda x: x['Loja'] == loja, vendedores))
    return maiorVendas(lista)


print('Melhor vendedor: {}'.format(melhorVendedor()))
