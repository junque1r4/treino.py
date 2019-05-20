lista = []
maior = menor = 0


for c in range(0, 5):
    lista.append(int(input(f'Digite o numero na posição [{c}]: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if maior < lista[c]:
            maior = lista[c]
        if menor > lista[c]:
            menor = lista[c]
        
print(f'O maior foi {maior} nas posições: ', end='')
for position, valor in enumerate(lista):
    if maior == valor:
        print(f'{position}...', end='')
print(f'\nO menor foi {menor} nas posições: ', end='')
for position, valor in enumerate(lista):
    if menor == valor:
        print(f'{position}...', end='')
print('\n')

