lista = (int(input('Digite o 1º valor: ')), int(input('Digite o 2º valor: ')), int(input('Digite o 3º valor: ')), int(input('Digite o 4º e último valor: ')))
if lista.count(9) >= 1:
	print('Quantidade de 9: ',lista.count(9))
else:
	print('Não foram digitados números 9!')

if 3 in lista:
	print('O primero 3 apareceu em: ',(lista.index(3)+1))
else:
	print('Não foram digitados números 3!')

contador = 0
for contador_par in range(0, 4):
	if lista[contador_par] % 2 == 0:
		contador += 1
print('Foram digitados: ',contador,'números pares')
