# Enunciado: Crie uma função multiplicador que recebe um número n e retorna uma lambda que multiplica qualquer número por n. Teste com n=3 e depois use a lambda para multiplicar 5.

def multiplicador(n):
    return lambda x: x * n

mult_3 = multiplicador(3)
print(mult_3(5))
