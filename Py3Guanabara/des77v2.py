palavras = ('aprender', 'programar', 'linguagem', 'python', 'estudar', 'praticar')

for palavra in palavras:
	print(f'\nNa palavra {palavra} temos: ', end='')
	for letra in palavra:
		if letra in 'aeiou':
			print(letra, end=' ')
print('\n')
