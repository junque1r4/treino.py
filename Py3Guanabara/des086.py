# Fazer uma matriz 3x3

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}]: '))

for m in range(0, 3):
    for k in range(0, 3):
        print(f'[{matriz[m][k]}]', end='')
    print()
