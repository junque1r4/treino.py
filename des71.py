print('='*30)
print('{:^30}'.format('Banco CEV'))
print('='*30)
valor = int(input('Digite um valor inteiro para saque: R$'))
cédulas = 50
total_cedulas = 0
while True:
	
	if valor >= cédulas:
		total_cedulas += 1
		valor -= cédulas
	else:
		if total_cedulas > 0:
			print(f'Total de {total_cedulas} cédulas de R${cédulas}')
		if cédulas == 50:
			cédulas = 20
		elif cédulas == 20:
			cédulas = 10
		elif cédulas == 10:
			cédulas = 1
		total_cedulas = 0
		if valor == 0:
			break
