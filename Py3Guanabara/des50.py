# Soma somente números pares!
pares = 0

for contador in range(1, 6+1):
    num_entrada = int(input('[*]: '))
    if num_entrada % 2 == 0:
        pares += num_entrada
print('[*] Total: ',pares)
       