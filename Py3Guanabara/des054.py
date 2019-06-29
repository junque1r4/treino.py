data_nascimento = 0
maior_idade = 0
menor_idade = 0
for c in range(0, 7):
    data_nascimento = int(input('[*]'))
    if 2019 - data_nascimento > 18:
        maior_idade += 1
    else:
        menor_idade += 1
print('Maior idade: %i\nMenor idade %i'%(maior_idade, menor_idade))