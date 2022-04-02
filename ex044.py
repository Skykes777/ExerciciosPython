print('\033[33m=-=\033[m'*10)
print('\033[33m=======ATACADO E VAREJOS======\033[m')
print('\033[33m=-=\033[m'*10)

preço = float(input('Preço do produto: R$'))
print('''FORMAS DE PAGAMENTO:
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no catão''')
pagamento = int(input('Qual a forma de pagamento? '))

if pagamento == 1:
    av = preço * 0.10
    avista = preço - av
    print(f'\033[32mPagamento a vista com 10% de desconto, valor total a pagar:\033[m \033[31mR${avista :.2f}')
elif pagamento == 2:
    avc = preço * 0.05
    avistaCartão = preço - avc
    print(f'\033[32m Pagamento a vista com 10% de desconto, valor total a pagar:\033[m \033[31mR${avistaCartão :.2f}')
elif pagamento == 3:
    pc2 = preço / 2
    print(f'\033[32m O pagamento em 2x no cartão fica:\033[m \033[31mR${pc2 :.2f}\033[m \033[33m do total de\033[m \033[31mR${preço :.2f}')
elif pagamento == 4:
    parcelas = int(input('Em quantas parcelas? ')) #Em quantas vezes a parcela
    js = preço * 0.20
    totalMaisJuros = preço + js #Juros principal
    parcelaMes = totalMaisJuros / parcelas #calculo de parcelas
    print(f'''\033[32mA compra será parcelada em \033[33m{parcelas}X\033[m \033[32mde\033[m \033[31mR${parcelaMes :.2f}\033[m \033[32mCOM JUROS DE 20%
Sua compra de\033[m \033[33mR${preço :.2f}\033[m \033[32mvai custar\033[m \033[31mR${totalMaisJuros :.2f}\033[m \033[32mno final.\033[m''')
else:
    print('Opção invalida, tente de novo!')
