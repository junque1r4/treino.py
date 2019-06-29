numero = 0
banco = 0
contador = 0
numero = int(input('Digite um número:[999 para parar] '))
while numero != 999:
	banco += numero
	contador += 1
	numero = int(input('Digite um número:[999 para parar] '))
print(f'Você digitou {contador} números e a soma de todos é: {banco}')
