from models.address import Address

class Property:
    def __init__(self, title: str,  square_footage: int, address: Address ):
        self.__title = title
        self.__square_footage = square_footage
        self.__addrees = address
        self.__imgs = []

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
        print(type(self.__addrees))
        return self.__addrees

    def add_property_photos(self, photo_img):
        self.__imgs.append(photo_img)


    def __str__(self):
        pass


    def to_dict(self):
        pass

    