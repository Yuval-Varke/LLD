from abc import ABC, abstractmethod
from vehicle import Vehicle


class FareStrategy(ABC):
    @abstractmethod
    def calFare(self, vehicle: Vehicle, distance: float) -> float:
        pass


class StandardFareStrategy(FareStrategy):
    def calFare(self, vehicle, distance):
        return vehicle.get_fare_amount() * distance


class SharedFareStrategy(FareStrategy):
    def calFare(self, vehicle, distance):
        return vehicle.get_fare_amount() * distance * 0.5


class LuxuryFareStrategy(FareStrategy):
    def calFare(self, vehicle, distance):
        return vehicle.get_fare_amount() * distance * 1.5