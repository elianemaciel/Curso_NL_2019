# Leia uma frase e exiba quantas vogais aparecem na frase.

frase = str(input('Digite uma frase: ')).upper()
contador = 0
for f in frase:
    for letra in f:
        if letra.lower() in 'aeiou':
            contador += 1
print('A frase digitada contém {} vogais.'.format(contador))
