def leiaInt(x=''):
    num = input(f'{x}')
    while num.isnumeric() == False:
        print(f'\033[0;31mERRO! {x}\033[m')
        num = input('Digite um número: ')
    return num


def leiaReal(x=''):
    num = input(f'{x}').replace(',', '.')
    while num.isnumeric() == False and '.' not in num:
        print(f'\033[0;31mERRO! {x}\033[m')
        num = input('Digite um número inteiro!')
    return float(num)

n = leiaInt('Digite um número: ')
i = leiaReal('Digite um número real: ')
print(f'Você acabou de digitar o número inteiro "{n}" e o inteiro "{i:.2f}"')