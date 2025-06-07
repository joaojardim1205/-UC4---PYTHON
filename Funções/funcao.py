def saudacao(nome):
    return f'Olé, {nome}'
print(saudacao('Joao'))

def soma(a, b):
    return a + b

resultado = soma(5, 4)
print(resultado)

def potencia(base, expoente = 2):
    return base ** expoente
print(potencia(3))
print(potencia(3, 3))

dobro = lambda x: x * 2
print(dobro(5))

soma = lambda a, b: a + b
print(soma(2, 3))
