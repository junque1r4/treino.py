primeiro_termo = int(input('[*] 1º Termo: '))
razao = int(input('[*] Razão: '))
contador = 0
for count in range(1, primeiro_termo, razao):
    print(count)
    contador += 1
    if contador >= 10:
        break
