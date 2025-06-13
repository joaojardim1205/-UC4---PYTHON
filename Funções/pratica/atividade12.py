# Enunciado: Dada uma lista de temperaturas em Celsius [9, 10, 20, 301, use map() e uma lambda para converter para Fahrenheit.
# Fórmula: F = (C9/5) + 32

temperaturas_celsius = [9, 10, 20, 30]

temperaturas_fahrenheit = list(map(lambda c: (c * 9 / 5) + 32, temperaturas_celsius))

print(temperaturas_fahrenheit)
