texto = "Vem tranquilo, vem tranquilo"
texto = texto.lower()
dic = {}

dic["A"] = texto.count("a")
dic["E"] = texto.count("e")
dic["I"] = texto.count("i")
dic["O"] = texto.count("o")
dic["U"] = texto.count("u")

print(dic)
