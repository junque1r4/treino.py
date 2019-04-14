print('Gerador de PA v3.0') # Título do programa
print('=-'*30) # Viadagenzinha
primeiro = int(input('Digite o primeiro termo: ')) # Primeiro termo da Progressão Aritmetica
razão = int(input('Digite a razão: ')) # Razão da PA
contador = 10 # Contador de termos a serem mostrados
contador_termos = 0 # Contador total de termos
while contador != 0: # Laço de repetição, poderia usar um while True: e um break na condição contador == 0 mas a atividade não permitia o uso do break!
	print(f'{primeiro} → ', end='') # Mostra o termo e uma setinha indicando o próximo termo
	primeiro += razão # soma do termo + a razão
	contador -= 1 # Diminui o contador para que o programa não seja infinito e que o valor digitado pelo usuário futuramente contenha o número de termos a serem mostrados.
	contador_termos += 1 # Contador total dos termos
	if contador == 0: # Estrutura de condição: para ver se o usuario deseja mais termos nessa PA
		contador = int(input(' PAUSA \nQuantos termos você deseja mostrar a mais?: '))
print(f'Final do programa. Foram postos: {contador_termos} termos') # Fim do programa

# Não interessa mas levei cerca de 3 minutos para fazer essa atividade, enquanto em outras mais fáceis eu levei 10 ~ 15 minutos.
