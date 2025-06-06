# Simule um sistema de login com while. O usuário tem 3 tentativas para acertar a senha
# "python123". Se errar, mostre "Tente novamente". Se acertar, mostre "Acesso permitido".

senha_correta = "python123"
tentativas = 3

while tentativas > 0:
    senha = input("Digite a senha: ")

    if senha == senha_correta:
        print("Acesso permitido")
        break
    else:
        tentativas -= 1
        if tentativas > 0:
            print("Tente novamente")
        else:
            print("Acesso bloqueado")