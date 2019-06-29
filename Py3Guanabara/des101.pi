from datetime import datetime


def voto(idade):
    print(f'Com {datetime.today().year - idade} anos: ', end='')
    if datetime.today().year - idade < 16:
        print('Não vota.')
    elif datetime.today().year - idade <= 18:
        print('Voto opcional')
    elif datetime.today().year - idade <= 70 :
        print('Voto obrigatório.')
    else:
        print('Voto opcional.')


print(datetime.today().year - 1999)
voto(1999)
voto(1910)