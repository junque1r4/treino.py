# Matriz, mas agora somando todos os números pares, todos os números da terceira coluna e o maior valor da terceira linha.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = 0
soma_coluna = 0
maior = 0

for c in range(0, 3):
    for k in range(0, 3):
        matriz[c][k] = int(input(f'Digite um valor para a posição [{c}, {k}]: '))
        if matriz[c][k] % 2 == 0:
            soma_pares += matriz[c][k]
        if matriz[c][2]:
            soma_coluna += matriz[c][2]
        if matriz[1][k] > maior:
            maior = matriz[1][k]

for z in range(0, 3):
    for x in range(0, 3):
        print(f'[{matriz[z][x]}]', end='')
    print()

print(f'A soma de todos os números pares é: {soma_pares}')
print((f'A soma de todos os números da 3ª coluna é: {soma_coluna}'))
print(f'O maior valor na segunda linha é: {maior}')