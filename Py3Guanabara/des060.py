# fatorial

número = int(input('Qual o número deseja tirar o fatorial: '))
contador = número
fatoração = 1

while contador > 0:
	print(f'{contador}', end='')
	print(' x ' if contador > 1 else ' = ', end='')
	fatoração *= contador
	contador -= 1

print(fatoração)
