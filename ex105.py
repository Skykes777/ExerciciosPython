def notas(*valores, sit=False):
    """
    -> Função para analisar notas e situações de varios alunos.
    :param (valores): Uma ou mais notas de alunos (aceita varias)
    :param (sit): Parametro opcional para mostra a situação da turma.
    :return: Um dicionário com varias situações da turma.
    """
    listNotas = {}
    listNotas['total'] = len(valores)
    listNotas['maior'] = max(valores)
    listNotas['menor'] = min(valores)
    listNotas['média'] = (sum(valores)) / len(valores)
    if sit:
        if listNotas['média'] >= 7:
            listNotas['situação'] = 'BOA'
        elif listNotas['média'] >= 5:
            listNotas['situação'] = 'RAZOÁVEL'
        else:
            listNotas['situação'] = 'RUIM'
    return listNotas

        
resp = notas(5.6, 7, 8.9, 3, sit=True)
print(resp)
