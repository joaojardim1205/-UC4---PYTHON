# Enunciado: Crie um programa que simule um jogo de dados: Use o módulo random para gerar um número aleatório entre 1 e 6. Peça ao usuário para adivinhar o número. Informe se ele acertou ou errou.

import random

def jogar_dado():
    numero_aleatorio = random.randint(1, 6)
    chute_usuario = int(input("Adivinhe o número do dado: "))
    if chute_usuario < 1 or chute_usuario > 6:
        print("Por favor, escolha um número entre 1 e 6.")
    elif chute_usuario == numero_aleatorio:
        print("Parabéns, você acertou!")
    else:
        print(f"Você errou! O número era {numero_aleatorio}.")

jogar_dado()