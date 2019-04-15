def toFahrenheit(celsius):
    return  celsius / 5 * 9 + 32

def toCelsius(fahrenheit):
    return  5 * (fahrenheit - 32) / 9

result = toCelsius(50)

print(result)