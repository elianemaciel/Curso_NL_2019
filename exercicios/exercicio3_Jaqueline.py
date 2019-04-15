# Leia uma frase e exiba quantas vogais aparecem na frase.

frase = str(input('Digite uma frase: ')).lower()
contador = 0
for letra in frase:
    if letra.lower() in 'aeiou':
        contador += 1
print('A frase digitada contém {} vogais.'.format(contador))
