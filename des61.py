print('Gerador de PA')
print('=='*15)
primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a Razão da PA: '))
contador1 = 10
contador2 = primeiro
while contador1 > 1:
	contador2 += razão
	contador1 -= 1
	print(f'{contador2} → ', end='')
print(' FIM')
