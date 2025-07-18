# Enunciado: Crie um programa que tente somar o número 5 com cada elemento de uma lista. Se houver algum item que não seja número, capture o erro e exiba uma mensagem informando.

valores = [5, 'a', 10, None, 3]

for valor in valores:
    try:
        resultado = 5 + valor
        print(f"5 somado a {valor} é {resultado}")
    except TypeError:
        print(f"Não é possível somar 5 com {valor}, pois não é um número.")