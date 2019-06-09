from random import randint
from operator import itemgetter
from time import sleep
jogo = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)}
print('\t\t<= Valores Sorteados =>')
for k, v in jogo.items():
    sleep(1)
    print(f'O {k} tirou {v} no dado')
rank = sorted(list(jogo.items()), key=itemgetter(1), reverse=True)
print('\t\t<= Ranking =>', end='\n')
for k, v in enumerate(rank):
    print(f'O {k + 1}º lugar ficou com {v[0]}, tirando {v[1]}')
    sleep(1.1)
