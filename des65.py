numero = float(input('Digite o valor: '))
maior_numero = menor_numero = soma = numero
contador = 1
continuar = str(input('Deseja continuar? [S ou N]')).strip().upper()
while continuar not in 'N':
	numero = int(input('Digite outro número[]: '))
	if numero >= maior_numero:
		maior_numero = numero
	if numero <= menor_numero:
		menor = numero
	contador += 1
	soma += numero
	continuar = str(input('Deseja continuar? [S ou N]')).strip().upper()

print(f'Você digitou {contador} números e a média entre eles é: {soma/contador:.2f}')
print(f'O maior valor foi {maior_numero} enquanto o menor foi {menor_numero}')
