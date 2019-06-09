aluno = dict()
aluno['Nome'] = str(input('Digite seu nome: '))
aluno['Média'] = float(input('Digite sua média.'))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif aluno['Média'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'

for k, v in aluno.items():
    print(f' - O {k} é igual a {v}')
