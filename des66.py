contador = soma = 0
while True:
	numero = int(input(f'[{contador+1}º]Número: '))
	if numero == 999:
		break
	contador += 1
	soma += numero
print(f'\nVocê digitou {contador} números e a soma é: {soma}')
