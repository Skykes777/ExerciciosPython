produtos = []
preços = []
preços_mais_mil = 0
soma = 0
condição = ''

print('\033[35m=-='*7)
print('>>VAREJO E ATACADÃO<<')
print('=-='*7)

while True:
    produto = input('\033[mNome do produto: ').strip().title() #-----NOME DOS PRODUTOS
    preço = float(input('Preço: R$')) #-----PREÇO DOS PRODUTOS
    produtos.append(produto)
    preços.append(preço)
    if preço > 1000: #-----PREÇOS MAIS DE 1000
        preços_mais_mil += 1
    soma += preço
    condição = input('Quer continuar? [S/N]: ').strip().upper()[0]
    while condição not in 'SN':
        condição = input('Quer continuar? [S/N]: ').strip().upper()[0]
    if condição == 'N':
        break
    else:
        print('\033[31m---'*10)
mais_barato_nome = produtos[preços.index(min(preços))]
mais_barato_preço = min(preços)
print('============FIM DA COMPRA============')
print(f'''Total da compra: R${soma:.2f}
Total de produtos acima de mil reais: {preços_mais_mil}
O produto mais barato foi: {mais_barato_nome} de RS{mais_barato_preço:.2f}''')
