cidade = input('Nome da cidade: ').strip()

lowerletra = cidade.lower() #tornando as letra minusculas para padronizar, mesmo o usuario esteja errando e colocando maiusculo com minusculo
junção = lowerletra.split() #ceparando as letras com split para pegar apenas o valor 0, independente do tamanho ou caso eu queria mudar a palavra de santo para outra frase
teste = 'santo' in junção[0] #aqui o teste irá perguntar se tem a frase santo na variavel junção no valor zero, sendo que 0 é a primeira palavra

print(f'A sua cidade começa com Santos: {teste}')
