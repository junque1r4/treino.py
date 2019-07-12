def ficha(nome='jogador', gols=0):
    nome = str(input('Nome do jogador: '))
    if nome == '':
        nome = 'jogador'
    gols = input('Número de gols: ')
    if gols.isnumeric() == False:
        gols = 0
    print(f'O {nome} marcou {gols} gol(s) no campeonato.')


ficha()