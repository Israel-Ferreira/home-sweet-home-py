from models.address import Address


class Property:

    """
    Class Property representa um Imóvel no sistema
    """

    def __init__(self, title: str,  square_footage: int, address: Address):
        self.__title = title
        self.__square_footage = square_footage
        self.__addrees = address

    @property
    def title(self):
        """
        title retorna o titulo do Anúncio
        """

        return self.__title

    @title.setter
    def title(self, new_title):
        self.__title = new_title

    @property
    def square_footage(self):
        """
        square_footage retorna a metragem da propriedade/imóvel em m**2
        """

        return self.__square_footage

    @property
    def address(self):
        """
        address retorna os dados de endereço do imóvel
        """

        print(type(self.__addrees))
        return self.__addrees

    def __str__(self):
        pass

    def to_dict(self):
        """
        to_dict converte os dados presentes no objeto em um dicionario
        """
