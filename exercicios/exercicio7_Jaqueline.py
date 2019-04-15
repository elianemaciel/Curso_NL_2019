# Escreva um programa que conta a quantidade de vogais em um texto
# e armazena tal quantidade em um dicionário, onde a chave é a vogal considerada.

frase = str(input('Digite uma frase: ')).lower()
dicionario = {}

dicionario['A'] = frase.count("a")
dicionario['E'] = frase.count("e")
dicionario['I'] = frase.count("i")
dicionario['O'] = frase.count("o")
dicionario['U'] = frase.count("u")

print(dicionario)
