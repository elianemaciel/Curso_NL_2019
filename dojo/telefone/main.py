lista = {"-": "-", "0": "0", "1":"1", 
          "A":2, "B":2, "C":2, 
          "D":3, "E":3, "F":3, 
          "G":4, "H":4, "I":4,
          "J":5, "K":5, "L":5, 
          "M":6, "N":6, "O":6, 
          "P":7, "Q":7, "R":7,
          "S":7, "T":8, "U":8, 
          "V":8, "X":9, "Y":9, 
          "W":9, "Z":9}

texto = input("Frase: ").upper()
resultado = ""
   

for i in texto:
  resultado += str(lista[i])

print(resultado)


