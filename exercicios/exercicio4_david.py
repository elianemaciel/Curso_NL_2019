#Crie um programa que recebe uma lista qualquer e:
#retorne o maior elemento
#retorne a soma dos elementos
#retorne o número de ocorrências do primeiro elemento da lista
#retorne a média dos elementos
#retorne o valor mais próximo da média dos elementos
#retorne a soma dos elementos com valor negativo
#retorne a quantidade de vizinhos iguais

lista= [10,20,30,40,50,60,70]
print("O maior numero é: ",max(lista))

print("A Soma dos numeros é ",sum(lista))

print("Numero de ocorrencias: ",lista.count(10))

soma= sum(lista)

media= soma/len(lista)

print("media: ",media)
