# No main.py, importe e use essas variáveis para calcular

from config import PI, GRAVIDADE

def calcular_area_circulo(raio):
    return PI * (raio ** 2)

def calcular_peso(massa):
    return massa * GRAVIDADE


raio = 10
area = calcular_area_circulo(raio)
print(f"A área do círculo com raio {raio} é: {area}")

massa = 50
peso = calcular_peso(massa)
print(f"O peso do objeto com massa {massa} kg é: {peso} N")