frase = input("Frase: ")

vogais = ["a", "e", "i", "o", "u"]
totalVogais = 0

for letra in frase:
    for vogal in vogais:
        if letra == vogal:
            totalVogais = totalVogais + 1

print(totalVogais)