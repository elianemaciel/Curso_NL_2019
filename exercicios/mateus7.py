dictVogais = {}

frase = input("Escreva uma frase: ")

vogais = ["A", "E", "I", "O", "U"]

for vogal in vogais:
    dictVogais[vogal] = frase.count(vogal) 

print(dictVogais)