from time import  sleep


def biggest(* num):
    big = 0
    tamanho = len(num)
    print('=-'*25, end='=\n')
    print('Analisando os valores...')
    if tamanho > 1:
        for x in num:
            print(x, end=' ')
            tamanho += 1
            sleep(0.3)
            if x > big:
                big = x
        print(f'Foram informados {tamanho} valores.')
        print(f'0 maior informado foi: {big}')
    else:
        print('Não foi informado valores.')

biggest(2, 9, 4, 5, 7, 1)
biggest(4, 7, 0)
biggest()
