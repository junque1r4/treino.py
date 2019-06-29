from datetime import date
cadastro = {'nome': str(input('Digite seu nome: ')), 'ano_nascimento': int(input('Digite o ano de nascimento: ')),
    'ctl': int(input('Digite sua carteira de trabalho (0 = Não possui): '))}
if cadastro['ctl'] != 0:
    cadastro['contrato'] = int(input('Ano de contratação: '))
    cadastro['sal'] = float(input('Digite o Salário: R$'))
    cadastro['aposentadoria'] = (date.today().year - cadastro['ano_nascimento'])
    cadastro['aposentadoria'] += ((cadastro['contrato'] + 35) - date.today().year)
print('=-' * 30, end='=\n')
for k, v in cadastro.items():
    print(f'.: {k.capitalize()} = {v}')
