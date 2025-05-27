tem_carteira = True
tem_idade = False

print('Pode dirigir?', tem_carteira and tem_idade)
print('Pode tentar?', tem_carteira or tem_idade)
print('Não pode?', not tem_idade)