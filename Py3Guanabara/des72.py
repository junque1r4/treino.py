contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
user = int(input('Digite um número de 0 a 20 para mostrarmos em extenso: '))
c = range(0, 21)
if user not in c:
	while True:
		user = int(input('Valor incorreto, somente números de 0 a 20 para mostrarmos em extenso: '))
		if 0 <= user <= 20:
			break
print('O número %d por extenso é: %s'%(user, contagem[user]))

# Usei a sintaxe do python2 só para não esquecer como se usa! *E porque o código fica mais rápido
# Mas normalmente uso o fstring que foi adicionado no python3.6
