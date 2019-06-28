pessoa = dict()
grupo = list()
idades = 0
meninas = list()
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo: [F/M]: ')).lower()[0]
    while pessoa['sexo'] not in 'fm':
        pessoa['sexo'] = str(input('Valor incorreto! Somente F e M: '))
    if pessoa['sexo'] == 'f':
        meninas.append(pessoa['nome'])
    pessoa['idade'] = int(input('Idade: '))
    idades += pessoa['idade']
    grupo.append(pessoa.copy())
    continuar = str(input('Deseja continuar? [S/N]: ')).lower()[0]
    while continuar not in 'sn':
        continuar = str(input('[S/N]? '))
    if continuar == 'n':
        break
print('=-=   '*7)
print(f'A) Pessoas cadastradas: {len(grupo)}')
print(f'B) Média de idade: {idades / len(grupo)}')
print(f'C) Temos', end='')
for k in meninas:
    print(f' {k}', end=',')
print(' de mulheres no grupo')
print('Lista das pessoas acima da média: ')
for p in grupo:
    if p['idade'] > (idades / len(grupo)):
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
    print()
print('<< Encerrado >>')
