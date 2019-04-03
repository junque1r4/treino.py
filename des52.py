# números primos
num = int(input('Primo:\n[*]:'))
primator = 0
for contador in range(1, num):
    if num % contador != 0:
        primator = + 1
print(primator+1)