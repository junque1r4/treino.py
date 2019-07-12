def leiaInt(x=''):
    num = input(f'{x}')
    while num.isnumeric() == False:
        print(f'\033[0;31mERRO! {x}\033[m')
        num = input('Digite um número: ')
    return num

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')