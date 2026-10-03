from location import Location
from vehicle import Vehicle


class Driver:
    def __init__(self, name, location: Location, vehicle: Vehicle):
        self.name: str = name
        self.location: Location = location
        self.vehicle: Vehicle = vehicle

    def get_location(self) -> Location:
        return self.location

    def set_location(self, location: Location) -> None:
        self.location = location    