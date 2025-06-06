# Use match para classificar um número em:
# ● "Positivo" (se > 0)
# ● "Negativo" (se < 0)
# ● "Zero" (se == 0).

numero = float(input("Digite um número: "))

match numero:
    case n if n > 0:
        print("Positivo")
    case n if n < 0:
        print("Negativo")
    case 0:
        print("Zero")