sexo = str(input('Digite seu sexo[M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
	sexo = str(input('Entrada incorreta, informe o sexo: [M/F]')).upper().strip()[0]
print('Dados registrados com sucesso!')
