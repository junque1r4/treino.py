alunos = list()
bank = list()  # Lista bank que irá guardar os valores.
while True:
    bank.append(input(f'\nDigite o nome do aluno: '))  # [x][0] // Nome
    bank.append(float(input('Digite a primeira nota: ')))  # [x][1]  //  Primeira nota
    bank.append(float(input('Digite a segunda nota: ')))  # [x][2]  //  Segunda nota
    alunos.append(bank[:])
    bank.clear()
    continuar = str(input('Deseja continuar? [S/N]'))[0].upper()
    if continuar == 'N':  # Quebra de laço
        break
print('=-'*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('=-'*30, end='=\n')
for x in range(0, len(alunos)):
    print(f'{x:<4}{alunos[x][0]:<10}{(alunos[x][1] + alunos[x][2]) / 2:>8.2f}')
print('=-'*30, end='=\n')
while True:
    notas = int(input('Você deseja saber as notas de qual aluno? [999 para parar]: '))
    if notas == 999:
        break
    print(f'As notas do(a) aluno(a) {alunos[notas][0]} são {alunos[notas][1], alunos[notas][2]}')
    print('=-'*30, end='=\n')
