# Use for e if para verificar se um número é primo (divisível apenas por 1 e ele mesmo).

numero = 17
primo = True

if numero < 2:
    primo = False
else:
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
            break

if primo:
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")