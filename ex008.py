media = float(input('Uma distancia em metros= '))
cm = media * 100
mm = media * 1000
km = media / 1000
print('A medida de {:.1f}m corresponde a..\n{} cm\n{} mm\n{} km'.format(media, cm, mm, km))