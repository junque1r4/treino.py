def escreva(str):
    leng = len(str) + 2
    print('~' * leng)
    print(f' {str}')
    print('~' * leng)


escreva(str(input('Digite uma frase: ')))
