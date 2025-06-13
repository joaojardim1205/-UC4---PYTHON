# Enunciado: Crie uma função contar_vogais que recebe uma string e retorna o número de vogais (a, e, i, o, u). Teste com "Python".

def contar_vogais(texto):
    return sum(1 for letra in texto.lower() if letra in 'aeiou')

print(contar_vogais("Python"))
