from models.property import Property
from models.address import Address


class Apartment(Property):

    def __init__(self, title: str, square_footage: int, address: Address , qty_bathrooms: int, qty_rooms: int, floor: int, pets_is_allowed=True):
        self.__qty_rooms = qty_rooms
        self.__qty_bathrooms = qty_bathrooms
        self.__floor = floor
        self.__pets_is_allowed = pets_is_allowed
        super().__init__(title, square_footage, address)

    @property
    def qty_rooms(self):
        return self.__qty_rooms

    @property
    def qty_bathrooms(self):
        return self.__qty_bathrooms

    @property
    def pets_is_allowed(self):
        return self.__pets_is_allowed

    @property
    def floor(self):
        return self.__floor
    
    def apartment_number(self):
        return self.__apartment_number
    
    def __str__(self):
        return f"Nome: {self.title}, Andar: {self.floor}, Metragem: {self.square_footage} m**2"
    

    def to_dict(self):
        return {
            "title": self.__title,
            "address": self.__addrees.to_dict(),
            "square_footage": self.__square_footage,
            "floor": self.__floor,
            "qty_bathrooms": self.__qty_bathrooms,
            "qty_rooms": self.__qty_rooms,
            "pets_is_allowed": self.__pets_is_allowed,
        }
    