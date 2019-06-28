jogador = dict()
jogador['nome'] = input('Qual o nome do(a) Jogador(a)? ')
partidas = int(input('Quantas partidas ele(a) jogou? '))
gols = list()
for x in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {x+1}? ')))
jogador['gols'] = gols.copy()
jogador['total'] = sum(gols)
print('=-'*30, end='=\n')
print(jogador)
print('=-'*30, end='=\n')
for k, v in jogador.items():
    print(f'O campo {k} tem {v}.')
print('=-'*30, end='=\n')
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for i, k in enumerate(jogador["gols"]):
    print(f"  => Na partida {i+1} ele fez {k} gols")
print(f"Foi um total de {jogador['total']} gols.")
