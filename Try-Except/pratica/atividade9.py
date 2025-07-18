# Enunciado: Crie uma função chamada dividir(a, b) que divide dois números e trata o caso em que b é zero.

def dividir(a, b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        return "Não é possível dividir por zero."

print(dividir(10, 2))
print(dividir(10, 0)) 