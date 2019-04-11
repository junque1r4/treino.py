from random import randint

pc = randint(1, 10)
jogador = pontos = 0
par_impar = ''
while True:
	jogador = int(input('Digite seu número: '))
	par_impar = str(input('Par ou impar? [P ou I]: ')).strip().upper()
	while par_impar not in 'PI':
		par_impar = str(input('Par ou Ímpar? [P ou I]: ')).strip().upper()[0]
	print('-='*30)
	if (jogador + pc) % 2 == 0 and par_impar == 'P':
		print(f'\nO pc escolheu {pc}.\nA soma foi {jogador+pc} e você escolheu {par_impar}.\n Parabéns pela vitória!:^30\n')
		pontos += 1
	elif (jogador + pc) % 2 != 0 and par_impar == 'I':
		print(f'\nO pc escolheu {pc}.\nA soma foi {jogador+pc} e você escolheu {par_impar}.\n Parabéns pela vitória!\n')
		pontos += 1
	else:
		print(f'\nO pc escolheu {pc}.\nA soma foi: {jogador+pc} e você escolheu {par_impar}, você perdeu!\n')
		break
	pc = randint(1, 10)
	print('-='*30)

print('Pontos = ',pontos)
