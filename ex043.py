peso = float(input('Quanto você pesa? '))
altura = float(input('Qual sua altura? '))
imc = peso / (altura**2)
print(f'Seu imc é: {imc :.1f}')
if imc < 18.5:
    print('Você está abaixo do peso!')
elif imc >= 18.5 and imc <= 25:
    print('Você está no peso ideial!')
elif imc <= 30:
    print('Vocẽ está com sobrepeso!')
elif imc <= 40:
    print('Você está com OBESIDADE!')
else:
    print('VocÊ está com OBESIDADE MORBIDA!')
