#Escreva um programa que conta a quantidade de vogais em um texto e armazena tal
#quantidade em um dicionário, onde a chave é a vogal considerada.

texto = "o rato rOeu a rOupa do rei"
texto = texto.lower()
dicionario={}

dicionario["A"]= texto.count("a")
dicionario["E"]= texto.count("e")
dicionario["I"]= texto.count("i")
dicionario["O"]= texto.count("o")
dicionario["U"]= texto.count("u")

print(dicionario)
