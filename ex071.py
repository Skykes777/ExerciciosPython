notas100 = 0
notas50 = 0
notas20 = 0
notas10 = 0
notas5 = 0
notas2 = 0
notas1 = 0

while True:
    print('=='*15)
    print('>>>>>>>>>BANCO VIAMÃO<<<<<<<<<')
    print('=='*15)
    valorSolicitado = int(input('Valor que desejá sacar? R$'))
    while valorSolicitado >= 100:
        notas100 += 1
        valorSolicitado -= 100
    while valorSolicitado >= 50:
        notas50 += 1
        valorSolicitado -= 50
    while valorSolicitado >= 20:
        notas20 += 1
        valorSolicitado -= 20
    while valorSolicitado >= 10:
        notas10 += 1
        valorSolicitado -= 10
    while valorSolicitado >= 5:
        notas5 += 1
        valorSolicitado -= 5
    while valorSolicitado >= 2:
        notas2 += 1
        valorSolicitado -= 2
    while valorSolicitado >= 1:
        notas1 += 1
        valorSolicitado -= 1
    if valorSolicitado == 0:
        break

print('=='*15)
print(f'''notas de 100: {notas100}
notas de 50: {notas50}
notas de 20: {notas20}
notas de 10: {notas10}
notas de 5: {notas5}
notas de 2: {notas2}
notas de 1: {notas1}''')
print('=========BANCO VIAMÃO=========')
