# Tabuada
print('''\nDigite o número final da tabuada, exemplo:
caso você escolha 5:
1 x 5
2 x 5
3 x 5
etc... ''')
fim = int(input('\nFIM [*]:'))
num = int(input('Digite o número para a tabuada [*] '))
for tabuada in range(1, fim+1):
    print(f'{num} x {tabuada} = {num*tabuada}')