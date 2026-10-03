class Location:
    def __init__(self, lat: float, long: float):
        self.__lat: float = lat
        self.__long: float = long

    def get_latitude(self) -> float:
        return self.__lat

    def get_longitude(self) -> float:
        return self.__long