def lerDinheiro(mensagem):
    valid = False
    while not valid:
        entrada = str(input(f'\033[0;33m{mensagem}\033[m')).replace(',', '.').strip()
        if entrada.isalpha():
            print(f'\033[0;31mErro! \033[0;33m"{entrada}"\033[0;31m não é um valor válido!\033[m')
        else:
            valid = True
            return float(entrada)

