#jaqueline e pedro
import random

# (random)Tendo como exemplo estas duas listas:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# Escreva um programa que retorne uma lista que contém apenas os elementos
# comuns entre as listas (sem elementos duplicados).
# Verifique se o seu programa funciona em duas listas de diferentes tamanhos.
# Extras:
# Gerar aleatoriamente duas listas para testar isso.
# Escreva isso em uma linha de Python

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = list()

for i in a:
    if i in b and i not in c:
        c.append(i)
print(c)

d = random.sample(range(100), k=32)
e = random.sample(range(100), k=22)
f = list()

for i in d:
    if i in e and i not in f:
        f.append(i)
print(f)

g = [i for i in d if i in e]

print(g)
