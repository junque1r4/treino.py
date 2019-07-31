from time import sleep

def lerCadastros():
    try:
        open('exerc.txt', 'r')
    except FileNotFoundError:
        open('exerc.txt', 'w+')
    arquivo = open('exerc.txt', 'r')
    for r in arquivo:
        print(r, end='')
    arquivo.close()


def leiaInt(x=''):
    num = input(f'{x}')
    while num.isnumeric() == False:
        print(f'\033[0;31mERRO! SOMENTE NÚMEROS INTEIROS!\033[m')
        num = input('Digite um número: ')
    return num


def inserirCadastro():
    arquivo = open('exerc.txt', 'a+')
    nome = input('Nome: ')
    idade = leiaInt('Idade: ')
    arquivo.write(f'{nome:<30}')
    arquivo.write(f'{idade}')
    arquivo.write('\n')
    arquivo.close()
    print(f'Novo registro de {nome} adicionado.\n')


def titulo(text='text'):
    tamanho = len(text) + 8
    print('=-' * tamanho, end='=\n|')
    print(text.center(tamanho * 2 - 1), end='|\n')
    print('=-' * tamanho, end='=\n')


def option(option1='s', option2='n', option3='exit', message='[S/N]: '):
    while True:
        choose = str(input(f'{message}'))
        if choose not in f'{option1}{option2}{option3}':
            print(f'\033[1;31mErro! "\033[m\033[4;30m{choose}\033[m\033[1;31m" não é uma das opções válidas!\033[m')
        else:
            break
    return choose


while True:
    titulo('Menu Principal') # TODO: Adicionar uma função para cores.
    print('\033[1;33m1\033[m - \033[0;34mMostrar os cadastros\033[m\n'
          '\033[1;33m2\033[m - \033[0;34mAdicionar novo cadastro\033[m\n'
          '\033[1;33m3\033[m - \033[0;34mSair do programa\033[m')
    optionMenu = option('1', '2', '3', '\033[1;33mChoose a option: \033[m')
    if optionMenu == '1':
        titulo('Cadastros') # TODO: Dominar o mundo!
        lerCadastros()
    if optionMenu == '2':
        titulo('Novo Cadastro')
        inserirCadastro()
    if optionMenu == '3':
        exit(9)
    sleep(2)
print('Obrigado!')
