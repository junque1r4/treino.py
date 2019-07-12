def fatorial(x, show=False):
    """
    -→ Calcula o Fatorial de um número.
    :param x: Fatorial a ser calculado.
    :param show: Mostra  os cálculos para a solução do programa.
    :return: Resultado do fatorial.
    """
    y = x
    while x != 1:
        if show:
            print(f'{x}', 'x ' if x > 2 else '= ', end='')
        x -= 1
        y *= x
    return y


print(fatorial(int(input('Função: ')), True))
