lista = []

for i in range(5):
    lista.append(int(input("Digite número: ")))


somaNegativos = 0 
for i in lista:
    if i < 0:
        somaNegativos = somaNegativos + i


print("--------------------------------------------")
print("Maior número: ",max(lista))
print("Soma dos elementos: ", sum(lista))
print("Número de ocorrências do primeiro elemento: ", lista.count(lista[0]))
print("Média dos elementos: ",sum(lista)/len(lista))
print("Soma dos valores negativos: ", somaNegativos)
print("Número de viznhos iguais: ")
for i in set(lista):
    print(i,"->",lista.count(i))