n_inteiro = 1
fibonacci = 0

n = int(input('Digite a quantidade de termos: '))

while n != 0:
	print(f'{fibonacci}', end=' → ')
	fibonacci = fibonacci + n_inteiro
	n_inteiro = fibonacci - n_inteiro
	n -= 1
print('FIM')
