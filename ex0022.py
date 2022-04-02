nome = input('Digite o nome: ')
maiusculo = nome.upper() #valor final
minusculo = nome.lower() #valor final

todasletras = nome.split()
juntarfrase = ''.join(todasletras)
lernometodo = len(juntarfrase) #valor final

primeironome = nome.split()
lernome = len(primeironome[0]) #valor final

print('Nome em maiusculo:{}\nNome em minusculo:{}\nValor de letras:{}\nQuantidade de letras no primerio nome:{}'.format(maiusculo, minusculo, lernometodo, lernome))
