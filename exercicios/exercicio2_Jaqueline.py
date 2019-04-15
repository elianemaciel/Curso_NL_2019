# Faça um programa que transforme uma temperatura fornecida em Celsius
# para a correspondente em Fahrenheit. A formula de conversão de Celsius
# para Fahrenheit é a seguinte: C = (5/9) * (F – 32).
# Obs: fazer conversão Fahrenheit para Celsius

f = float(input('Digite a temperatura em graus em Fahrenheit: '))
c = (5 / 9) * (f - 32)
print('Temperatura {:.1f}°C em graus Fahrenheit equivale à {:.1f}°F graus Celsius.'.format(c, f))
