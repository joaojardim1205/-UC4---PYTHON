# Use while para somar números até que o total seja maior que 100. A cada iteração, imprima o total.

total = 0

while total <= 100:
    numero = float(input("Digite um número para somar: "))
    total += numero
    print(f"Total atual: {total}")