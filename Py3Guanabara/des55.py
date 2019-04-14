maior_peso = 0
menor_peso = 9*99
peso = 0
for c in range(1, 7):
    peso = float(input('Digite o peso da %iª pessoa: '%c))
    if peso > maior_peso:
        maior_peso = peso
    if peso < menor_peso:
        menor_peso = peso
print('Maior peso:%i\nMenor peso:%i'%(maior_peso, menor_peso))