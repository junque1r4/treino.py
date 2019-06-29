from random import randint
from time import sleep


def sorteia(lista):
    print('Os valores ', end='')
    for x in range(0, 5):
        lista.append(randint(0, 10))
    for x in range(0, len(lista)-1):
        if x == 3:
            print(lista[x], end=' ')
        else:
            print(lista[x], end=', ')
    sleep(0.6)
    print(f'e {lista[-1]} foram adicionados a lista.')


def soma_par(lista):
    soma = int()
    print(f'Somando os valores: {lista},  temos: ', end='')
    for z in lista:
        if z % 2 == 0:
            soma += z
    print(soma, 'números pares')


listinha = list()
sorteia(listinha)
soma_par(listinha)
