frase="o rato roeu a roupa do rei "
frase=frase.lower()
dicionario={}
dicionario["A"]= frase.count("a")
dicionario["E"]= frase.count("e")
dicionario["I"]= frase.count("i")
dicionario["O"]= frase.count("o")
dicionario["U"]= frase.count("u")

print(dicionario)
