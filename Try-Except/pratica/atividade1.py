# Enunciado: Crie um programa que tente dividir o número 10 por diferentes valores armazenados em uma lista. Use try e except para capturar o erro que ocorre quando o divisor é 0 e imprima uma mensagem amigável nesse caso.

valores = [2, 0, 5, 10, 0, 3]

for valor in valores:
    try:
        resultado = 10 / valor
        print(f"10 dividido por {valor} é {resultado}")
    except ZeroDivisionError:
        print("Não é possível dividir por zero.")
