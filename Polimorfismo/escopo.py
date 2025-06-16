def minha_funcao():
    x = 10
    print(x)

minha_funcao()
#print(x) #Gera um erro x não existe fora da função

y = 20

def imprimir_7():
    print(y)

imprimir_7()
print(y)

z = 30

def alterar_z():
    global z
    z = 40

print(z)
alterar_z()
print(z)
