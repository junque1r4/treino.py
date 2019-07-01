def fatorial(x, show=False):
    y = x
    while x != 1:
        if show:
            print(f'{x}', 'x ' if x > 2 else '= ', end='')
        x -= 1
        y *= x
    print(y)


fatorial(int(input('Função: ')), True)
