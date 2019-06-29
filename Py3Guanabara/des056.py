contador_idade = 0
contador_novinhas = 0
contador_peludos = 0
contador_peludo_velho = ''
for c in range(1, 5):
    nome = str(input('Nome: ')).strip()
    sexo = input('[M/F]: ').strip().upper()
    idade = int(input('Idade: '))
    contador_idade += idade
    if sexo == 'F' and idade < novinha_velha: 
        contador_novinhas += 1
    if sexo == 'M':
        if idade > contador_peludos:
            contador_peludos = idade
            contador_peludo_velho = nome


media = contador_idade/4            
print(f'A média de idade do grupo é: {media}\nA quantidade de meninas menores de 20 é: {contador_novinhas}')
if contador_peludos >= 1: 
    print(f'O homem mais velho foi {(contador_peludo_velho).title()} com {contador_peludos} anos')        