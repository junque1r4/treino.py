from des109 import moeda

valor = int(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(valor)} é {moeda.metade(valor, False)}')
print(f'O dobro de {moeda.moeda(valor)} é {moeda.dobro(valor)}')
print(f'Aumentando 10%, temos {moeda.aumentar(valor, 10)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(valor, 13)}')
