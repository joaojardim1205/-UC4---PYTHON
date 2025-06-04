# Enunciado: Classifique um triângulo com lados 5, 5 e 5.

a = 5
b = 5
c = 5
if a == b == c:
    print("Equilátero")
elif a == b or a == c or b == c:
    print("Isósceles")
else:
    print("Escaleno")