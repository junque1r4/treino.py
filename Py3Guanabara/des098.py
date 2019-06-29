from time import sleep


def contagem(inicio, fim, passo):
    if passo == 0:
        passo += 1
    if fim <= 0 and passo >= 0:
        passo -= passo*2
    print('=-' * 25, end='=\n')
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(1.5)
    for x in range(inicio, fim, passo):
        print(f'{x}', end=', ')
        sleep(0.5)
    print(f'{fim}.')
    print('=-' * 25, end='=\n')


contagem(0, 10, 1)
contagem(10, 1, -1)
print('  Personalize a sua contagem! ')
start = int(input('Início: '))
end = int(input('Fim: '))
feet = int(input('Passo: '))
contagem(start, end, feet)
