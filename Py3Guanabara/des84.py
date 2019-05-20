temporário = []
nomes_maiores = []
nomes_menores = []
maior = menor = total = 0
continuar = 'S'
while continuar not in 'N':
    temporário.clear()
    temporário.append(str(input('Nome: ')))
    temporário.append(float(input('Peso: ')))
    total += 1
    if total == 1:
        maior = menor = temporário[1]
    if temporário[1] > maior:
        maior = temporário[1]
        nomes_maiores.clear()
        nomes_maiores.append(temporário[0])
    elif temporário[1] == maior:
        nomes_maiores.append(temporário[0])
    if temporário[1] < menor:
        menor = temporário[1]
        nomes_menores.clear()
        nomes_menores.append(temporário[0])
    elif temporário[1] == menor:
        nomes_menores.append(temporário[0])
    continuar = str(input('Deseja continuar? [S] ou [N]: ')).upper()[0]
print(f'\nVocê cadastrou {total} pessoas.')
print(f'Maior peso: {maior}Kg.\nPessoas com esse peso: {nomes_maiores}')
print(f'Menor: {menor}Kg.\nPessoas com esse peso: {nomes_menores}')