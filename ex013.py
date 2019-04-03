init = int(input('Digite o inicio: '))
fin = int(input('Digite o fim: '))
pulos = int(input('De quantos em quantos pulos?: '))
soma = 0
for c in range(init, fin, pulos):
    teste = int(input('Digite um valor: '))
    soma += teste
    print(c)
    print(soma)
print('FIM')