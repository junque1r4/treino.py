def moeda(valor=0, tipo='R$'):
    return f'{tipo}{valor:.2f}'.replace('.', ',')


def metade(valor=0):
    return valor / 2


def dobro(valor=0):
    return valor * 2


def aumentar(valor=0, aumento=0):
    return valor + (aumento * (valor / 100))


def diminuir(valor=0, porcentagem=0):
    return valor - (porcentagem * (valor / 100))
