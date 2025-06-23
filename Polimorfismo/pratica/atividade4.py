# Crie uma função contador() que retorna uma função interna incrementar(), que aumenta um contador interno toda vez que é chamada

def contador():
    count = 0
    def incrementar():
        nonlocal count
        count += 1
        return count
    return incrementar

inc = contador()
print(inc())
print(inc())
print(inc())
