lista = list()
lista_par = list()
lista_imp = list()
coletor = 0

while True:
    coletor = int(input('Digite o número a ser adicionado: '))
    lista.append(coletor)
    if coletor % 2 == 0:
        lista_par.append(coletor)
    else:
        lista_imp.append(coletor)
    continuar = str(input('Deseja continuar? [S ou N]')).upper()[0]
    if continuar in 'N':
        break

print(f'Aqui está a lista com todos os valores:\n{lista}\n Todos os valores pares:\n{lista_par}\nTodos os valores Ímpares:\n{lista_imp}')
