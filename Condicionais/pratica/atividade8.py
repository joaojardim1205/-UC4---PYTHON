# Enunciado: Verifique se o ano 2024 é bissexto.

ano = 2024
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("Ano bissexto")
else:
    print("Ano não bissexto")