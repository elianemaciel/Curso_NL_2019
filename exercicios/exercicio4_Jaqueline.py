# Crie um programa que recebe uma lista qualquer e:
# retorne o maior elemento
# retorne a soma dos elementos
# retorne o número de ocorrências do primeiro elemento da lista
# retorne a média dos elementos
# retorne o valor mais próximo da média dos elementos
# retorne a soma dos elementos com valor negativo
# retorne a quantidade de vizinhos iguais

lista = [10, 9, 6, 8, 50, 40, 10]

soma = sum(lista)
media = soma / len(lista)

print('O maior elemento é: {}.'.format(max(lista)))
print('A soma dos elementos da lista é: {}.'.format(sum(lista)))
print('Número de ocorrências do primeiro elemento da lista: {}.'.format(lista.count(10)))
print('Média dos elementos da lista: {}.'.format(media))
print('Valor mais próximo da média: {}.'.format())
