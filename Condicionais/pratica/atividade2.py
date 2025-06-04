# Enunciado: Verifique a situação eleitoral para uma idade de 17 anos.

idade = 17
if idade < 16:
    print("Não pode votar")
elif 16 <= idade < 18 or idade > 70:
    print("Voto facultativo")
else:
    print("Voto obrigatório")