# Crie uma variável global contador 0. Depois, defina uma função incrementar () que usa uma variável local contador e tenta modifica-la
# Mostre que a variável global não é alterada.

contador = 0

def incrementar():
    contador = 10
    contador += 1
    print("Valor dentro da função:", contador)

incrementar()
print("Valor fora da função:", contador)
