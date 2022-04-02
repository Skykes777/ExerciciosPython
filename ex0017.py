import math
cat1 = float(input('Cateto oposto: '))
cat2 = float(input('Cateto adjacente: '))
resultado = math.hypot(cat1, cat2)
print(f'A hipotenuza desse triângulo-retangulo é {resultado :.2f}.')