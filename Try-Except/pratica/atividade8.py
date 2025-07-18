# Enunciado: Modifique o exercício anterior para adicionar um bloco finally que imprime uma mensagem sempre, independentemente de erro.

valores = [10, 0, 'a', [1, 2, 3], 5]

for valor in valores:
    try:
        resultado_divisao = 100 / valor
        print(f"100 dividido por {valor} é {resultado_divisao}")
        
        lista = [1, 2, 3]
        print(f"Elemento na posição {valor} da lista é {lista[valor]}")
        
        resultado_int = int(valor)
        print(f"O valor {valor} convertido para inteiro é {resultado_int}")  
    except ZeroDivisionError:
        print("Não é possível dividir por zero.")
    except IndexError:
        print(f"Erro: índice {valor} fora do limite da lista.")
    except TypeError:
        print(f"Erro: não é possível realizar a operação com o valor '{valor}'.")
    finally:
        print("Tentativa de processamento concluída.\n")