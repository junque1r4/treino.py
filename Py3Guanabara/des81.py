valores_user = []

while True:
    valores_user.append(int(input('Digite um valor para ser adicionado: ')))
    continuar = str(input('Deseja continuar?\n[S]im ou ENTER para continuar\n[N]ão para parar: ')).upper()
    if continuar == 'N':
        break
valores_user.sort(reverse=True)
print(f'Você digitou os seguintes valores: {valores_user}')
print(f'Número de caracteres na lista: {len(valores_user)}')
if 5 in valores_user:
    print('O valor 5 está na lista!')
else:
    print('O valor 5 não está na lista!')