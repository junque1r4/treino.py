def cdt(x, y):
    area = x * y
    print(f'A área de um terreno {x}x{y} é de {area}m²')


print('Controle de Terrenos')
print('-'*10)
larg = float(input('LARGURA [m]: '))
comp = float(input('COMPRIMENTO [m]: '))
cdt(larg, comp)
