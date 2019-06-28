jogador = dict()
cadastros = list()
gols = list()
while True:
    jogador['nome'] = input('Qual o nome do(a) Jogador(a)? ')
    partidas = int(input('Quantas partidas ele(a) jogou? '))
    for x in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {x+1}? ')))
    jogador['gols'] = gols.copy()
    jogador['total'] = sum(gols)
    cadastros.append(jogador.copy())
    continuar = str(input('Deseja continuar [S/N]? ')).upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Valor incorreto, somente [S/N]')).upper()[0]
    if continuar == 'N':
        break
print('=-= '*20, end='=\n')
print('cod:    nome:        gols:        total:')
for k, v in enumerate(cadastros):
    print(f' .:{k:>3}', end=' '*7)
    for d in v.values():
        print(f'.:{str(d):<12}', end='')
    print()
while True:
    busca = int(input('Mostar dados de qual jogador? [999] para parar: '))
    if busca == 999:
        break
    if busca >= len(cadastros):
        print(f'Erro não existe nenhum jogador com o código {busca}!')
    else:
        print(f' == * LEVANTAMENTO DO JOGADOR {cadastros[busca]["nome"]}:')
        for i, g in enumerate(cadastros[busca]['gols']):
            print(f'        No jogo {i+1} ele fez {g} gols.')
    print('-' * 35)
print('<< VOLTE SEMPRE >>')
