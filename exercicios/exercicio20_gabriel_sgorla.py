'''exercicio feito por David, Gabriel Rech e Gabriel Sgorla'''
import random
lista1 = random.sample(range(0,20),5)
lista2 = random.sample(range(0,20),10)
lista3 = []

print(lista1)
print("----------------------------------------------------------")
print(lista2)
print("----------------------------------------------------------")
'''for i in lista1:
    if i in lista2:
        lista3.append(i)
print(lista3)'''

print([i for i in lista1 if i in lista2])
