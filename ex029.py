velocidade = float(input('Velocidade do carro: '))
multa = (velocidade - 80)*7
if velocidade > 80:
    print(f'Você foi multado por ultrapassar o limite de 80km/h, multa a pagar de R${multa :.2f}')
else:
    print('Tenha um bom dia, use sempre cinto de segurança!')