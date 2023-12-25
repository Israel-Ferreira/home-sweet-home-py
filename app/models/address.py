class Address:

    def __init__(self, public_place, number, neighborhood, city, state, country, latitude, longitude, complement=""):
        self.__public_place = public_place
        self.__number = number
        self.__neighborhood = neighborhood
        self.__city = city
        self.__state = state

        self.__country = country

        self.complement = complement

        self.__latitude = latitude
        self.__longitude = longitude


    @property
    def public_place(self):
        return self.__public_place
    
    @public_place.setter
    def public_place(self, public_place):
        if public_place is None or public_place == "":
            raise RuntimeError()
        

        self.__public_place = public_place


    @property
    def country(self):
        return self.__country
    

    @property
    def number(self):
        return self.__number
    
    @property
    def city(self):
        return self.__city
    
    @property
    def neighborhood(self):
        return self.__neighborhood
    

    @property
    def state(self):
        return self.__state
    
    @property
    def latitude(self):
        return self.__latitude
    
    @property
    def longitude(self):
        return self.__longitude
    

    def to_dict(self):
        return {
            "public_place": self.__public_place,
            "number": self.__number,
            "neighborhood": self.__neighborhood,
            "city": self.__city,
            "state": self.__state,
            "country": self.__country,
            "complement": self.complement,
            "latitude": self.__latitude,
            "longitude": self.__longitude
        }