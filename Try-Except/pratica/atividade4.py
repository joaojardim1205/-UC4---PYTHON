# Enunciado: Crie uma lista com diferentes tipos de dados (número como string, letras, valores nulos) e tente convertê-los para int. Capture os erros ao tentar converter valores inválidos.

valores = ['10', '20', 'a', None, '30']

for valor in valores:
    try:
        resultado = int(valor)
        print(f"O valor {valor} convertido para inteiro é {resultado}")
    except (ValueError, TypeError) as e:
        print(f"Não foi possível converter {valor} para inteiro: {e}")