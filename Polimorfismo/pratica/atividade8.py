# Mostre que variáveis criadas em if ou for vazam para o escopo externo em Python.

if True:
    x = 10

print(x)

for i in range(3):
    y = i * 2

print(y)