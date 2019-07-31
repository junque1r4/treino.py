from time import sleep


colorido = (
    '\033[m',          # 0 → Sem COr
    '\033[0;30;41m',    # 1 → Vermelho
    '\033[0;30;42m',    # 2 → Verde
    '\033[0;30;43m',    # 3 → Amarelo
    '\033[0;30;44m',    # 4 → Azul
    '\033[0;30;45m',    # 5 → Roxo
    '\033[7;30m'       # 6 → Branco
    )


def titulo(frase, cor=5):
    tamanho_frase = len(frase) + 4
    print(colorido[cor], end='')
    print('~' * tamanho_frase)
    print(frase)
    print('~' * tamanho_frase)
    print(colorido[0])

def ajuda(function):
    print(f'Aqui temos o manual em (EN) da função {function}')
    sleep(1)
    help(function)
    sleep(2)


while True:
    titulo('Sistema interativo PyHelp')
    comando = str(input('Função ou Biblioteca:\n>>> '))
    if comando.lower() == 'fim':
        break
    else:
        ajuda(comando)
