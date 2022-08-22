class Funcionario:
    def __init__(self, nome: str, idf: int) -> None:
        self.__nome = nome
        self.__idf = idf
    
    def mostrar_Funcionario(self) -> None:
        return self.__nome, self.__idf

###############################################################

class Empresa:
    def __init__(self) -> None:
        self.fun = []
        while True:
            op = input('''[1] Adicionar funcionário
[2] Mostrar funcionário
opção: ''').strip()[0]
            if op == '1':
                self.__adiconar_Fun()
            elif op == '2':
                self.__mostrar_Fun()
            else:
                self.__erro()
    
    def __adiconar_Fun(self) -> None:
        nome = input('Digite o nome do novo funcionário: ').strip().title()
        idf = int(input('Digite os 4 números de identificação do funcionário: '))
        self.fun.append(Funcionario(nome, idf))
    
    def __mostrar_Fun(self) -> None:
        for i, f in enumerate(self.fun):
            print(f'{i+1:2}º: {f.mostrar_Funcionario()}')
    
    def __erro(self) -> None:
        print('Opção invalida...')

###############################################################

empres1 = Empresa()
