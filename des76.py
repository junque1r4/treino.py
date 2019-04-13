print('-'*36)
print('|{:^34}|'.format('Nota fiscal'))
print('-'*36)
compras = ('Coca-Cola', 4.75, 'Pão Fôrma', 3.00, 'Queijo em Tara', 2.75, 'Biscotos', 7.65, 'Iogurte 1l', 3.00)
for repetidor in range(0, len(compras)):
	if repetidor % 2 == 0:
		print('|{:.<26} R${:.2f} |'.format(compras[repetidor], compras[repetidor+1]))
print('-'*36)
print('|  Lojinha DESGRAÇA, volte sempre! |')
print('-'*36)

