palavras = ('aprender', 'programar', 'python', 'shit', 'linguagem', 'praticar', 'mercado', 'futuro', 'curso', 'gratis')
for repetição in range(0, len(palavras)):
	print(f'Na palavra {palavras[repetição]} temos: ', end='')
	if 'a' in palavras[repetição]:
		if palavras[repetição].index('a') >= 0:
			print('a', end=' ')
		else:
			print(' ')

	if 'e' in palavras[repetição]:
		if palavras[repetição].index('e') >= 0:
			print('e', end=' ')
		else:
			print(' ')

	if 'i' in palavras[repetição]:
		if palavras[repetição].index('i') >= 0:
			print('i', end=' ')
		else:
			print(' ')


	if 'o' in palavras[repetição]:
		if palavras[repetição].index('o') >= 0:
			print('o', end=' ')
		else:
			print(' ')

	if 'u' in palavras[repetição]:
		if palavras[repetição].index('u') >= 0:
			print('u', end=' ')
		else:
			print(' ')
	print('\n')
