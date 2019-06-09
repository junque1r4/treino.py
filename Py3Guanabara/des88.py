from time import sleep
from random import randint

print('='*30, end='\n=')
print(f'{"Joga na MEGA":^28}', end='=\n')
print('='*30)  # Título e início do código.

teste = 0
jogos = int(input('Quantos jogos você quer ver? '))
cartela = list()

for c in range(0, jogos):
    cartela.clear()
    while True:
        teste = randint(0, 60)
        if teste not in cartela:
            cartela.append(teste)
        if len(cartela) == 6:
            break
    sleep(1)
    print(sorted(cartela))
    jogos -= 1

print(f'{" > ! Boa Sorte ! < ":=^29}', end='=\n')
