from math import sqrt


class Location:
    def __init__(self, lat: float, long: float):
        self.__lat: float = lat
        self.__long: float = long

    def get_latitude(self) -> float:
        return self.__lat

    def get_longitude(self) -> float:
        return self.__long

    def calcDistance(self, loc: Location):
        # Euclidean Distance
        dx: float = self.get_latitude() - loc.get_latitude()
        dy: float = self.get_longitude() - loc.get_longitude()
        return sqrt(dx * dx + dy * dy)