idade = 16

if idade >= 18:
    print('Maior de idade!')
else:
    print('Menor de idade!')

nota = 7.5

if nota >= 9:
    print('Conceito A')
elif nota >= 7:
    print('Conceiot B')
elif nota >= 5:
    print('Conceito C')
else:
    print('Conceito D')

idade = 17
tem_autorizacao = True

if idade >= 18:
    print('Acesso permitido')
else:
    if tem_autorizacao:
        print('Acesso com autorização')
    else:
        print('Acesso negado')

