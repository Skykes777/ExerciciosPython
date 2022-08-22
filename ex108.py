# usando classmethod para metodo de classe

class Loja:
    tarifa = 1.03
    def __init__(self, endereço: str) -> None:
        self.__endereço = endereço

    def apresentar_endereço(self) -> None:
        print(self.__endereço)

    @classmethod
    def vender(cls) -> int:
        return 40 * cls.tarifa

    @classmethod
    def alterar_tarifa(cls, nova_tarifa: int) -> None:
        cls.tarifa = nova_tarifa
    
lojaCentro = Loja('Centro')

print(lojaCentro.vender())
lojaCentro.alterar_tarifa(1.10)
print(lojaCentro.vender())
