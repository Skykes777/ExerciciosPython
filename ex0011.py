largura = float(input('largura da parede: '))
metros = float(input('altura em metros: '))
area = largura * metros
ltinta = area / 2
print('A dimensão de {:.2f}x{:.2f} tem sua área de {:.2f}m².\nSerá necessário {:.2f}l de tinta para pintar a parede.'.format(largura, metros, area, ltinta))
