# Use while para somar os dígitos de um número (ex: 123 → 1 + 2 + 3 = 6).

numero = 123
soma = 0

while numero > 0:
    soma += numero % 10
    numero //= 10

print(f"A soma dos dígitos é {soma}.")