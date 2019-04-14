from random import randint

print('Eu estou pensando em um número de 0 a 10, você consegue adivinha-lo?')
pc = randint(0, 10)
contador = 0

while True:
	jogador = int(input('Número apostado: '))
	contador += 1
	if jogador == pc:
		break
	elif jogador > pc:
		print('hmm... menos!')
	elif jogador < pc:
		print('hmm... mais!')

print(f'\nParabéns! \n Você tentou {contador}x')
