# Esse code tá uma putaria cheia de gambiarra!
lista = ('Athletico-PR', 'Atlético-MG', 'Avaí', 'Bahia', 'Botafogo', 'CSA', 'Ceará', 'Chapecoense', 'Corinthians', 'Cruzeiro', 'Flamengo', 'Fluminese', 'Fortaleza', 'Goiás', 'Grêmio', 'Internacional', 'Palmeiras', 'Santos', 'São Paulo', 'Vasco')

print('=-'*35)
print('Os 5 primeiros são: ', end='') # Gambiarra
for lista1 in range(0,5): # Gambiarra
	if lista1 < 4:
		print(lista[lista1], end=' → ')
	else:
		print(lista[lista1], end='.\n')
print('=-'*35)
print('Os últimos são: ', end='') # Gambiarra
for lista2 in range(16, 20):
	if lista2 < 19:
		print(lista[lista2], end=' → ')
	else:
		print(lista[lista2], end='.\n')
print('=-'*35)
print('Lista organizada: ', end='') # Gambiarra!
for organizado in sorted(lista):
	if organizado == 'Vasco': 
		print(organizado, end='.\n')
	else:
		print(organizado, end=', ')
print('=-'*35)
print('Posição da Chapecoense: ', (lista.index('Chapecoense'))+1)
print('=-'*35)

# MUITA GAMBIARRA!
# Futuramente quando eu aprender novas funcionalidades eu vou fazer uma v2.0 desse code.
