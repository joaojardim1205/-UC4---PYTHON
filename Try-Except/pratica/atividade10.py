# Enunciado: Crie um programa que tenta multiplicar valores de uma lista por 2. Se o valor não for um número, mostre uma mensagem personalizada com o tipo do erro.
 
valores = [2, 5, None, 3.5]

for valor in valores:
    try:
        resultado = valor * 2
        print(f"{valor} multiplicado por 2 é {resultado}")
    except TypeError as e:
        print(f"Erro ao tentar multiplicar {valor}: {e}")