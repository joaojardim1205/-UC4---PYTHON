# Use match para verificar se uma letra é uma vogal (a, e, i, o, u). Se não for, exiba "Não é vogal".

letra = input("Digite uma letra: ").lower()

match letra:
    case 'a' | 'e' | 'i' | 'o' | 'u':
        print("É uma vogal")
    case _:
        print("Não é vogal")