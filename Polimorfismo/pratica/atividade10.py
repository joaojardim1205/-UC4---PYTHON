# Crie uma função extema contador() que mantém um contador interno e retorna uma função que o incrementa usando nonlocal

def contador():
    count = 0
    def incrementar():
        nonlocal count
        count += 1
        return count
    return incrementar

cont = contador()
print(cont())
print(cont())
print(cont())
