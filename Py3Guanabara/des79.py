'''
Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os
em uma lista. Caso o número já exista lá dentro ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados em ordem crescente. 
'''

lista = []
while True:
    cofre = int(input('\nDigite o valor a ser adicionado: '))
    if cofre in lista:
        print('Valor já contido na lista, vão vou adicionar!')
    else:
        lista.append(cofre)
        print('Valor adicionado com sucesso.')
    parada = str(input('Deseja adiconar mais?\n[S]im ou [N]ão: ')).upper()[0]
    if parada in "N":
        break
lista.sort()
print(f'\nA lista adicionada contém os seguintes valores: {lista}')
