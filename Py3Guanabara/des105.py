def notas(*notas, sit=False):
    turma = dict()
    turma['maior'] = max(notas)
    turma['menor'] = min(notas)
    turma['média'] = sum(notas)/len(notas)
    if sit:
        if turma['média'] > 7:
            turma['situação'] = 'Ótima'
        elif turma['média'] > 5:
            turma['situação'] = 'Razoável'
        else:
            turma['situação'] = 'Ruim'
    return turma


x = notas(9, 9, 9, 9, sit=True)
print(x)