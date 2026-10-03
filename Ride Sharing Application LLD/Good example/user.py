from location import Location
from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, name: str, email: str, location: Location):
        self.name = name
        self.email = email
        self.location = location

    def get_location(self):
        return self.location

    def set_location(self, new_location: Location):
        self.location = new_location

    @abstractmethod
    def notify(self):
        pass