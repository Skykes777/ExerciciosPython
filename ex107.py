class Cadastro:
    def __init__(self) -> None:
        nome = input('Digite seu nome: ').strip()
        idade = int(input('Sua idade: '))
        senha = input('Crie uma senha: ').strip()
        if self.__teste_dados(nome, idade, senha) == True:
            teste = self.__teste_senha(senha)
            if teste == True:
                self.__dados_cliente(nome, idade)
            else:
                self.__erro()
        else:
            self.__erro()

    def __teste_dados(self, nome: str, idade: int, senha: str) -> bool:
        if isinstance(nome, str) and isinstance(idade, int) and isinstance(senha, str) and idade >= 18:
            return True
        else:
            return False

    def __teste_senha(self, senha: str) -> bool:
        testS = input('Digite sua senha: ').strip()
        if testS == senha:
            return True
        else:
            return False

    def __dados_cliente(self, nome, idade):
        print(f'''Dados do cliente {nome} com idade de {idade} anos.''')

    def __erro(self):
        print('Erro na entrada de dados.')

cad1 = Cadastro()
