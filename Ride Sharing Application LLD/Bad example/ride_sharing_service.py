from typing import List
from driver import Driver
from passenger import Passenger
from location import Location
from math import sqrt
from vehicle import Vehicle


class RideSharingServiceApp:
    def __init__(self):
        self.drivers: List[Driver] = []
        self.passengers: List[Passenger] = []

    # Method to add driver
    def add_driver(self, driver: Driver):
        self.drivers.append(driver)

    # Method to add a passenger
    def add_passenger(self, passenger: Passenger):
        self.passengers.append(passenger)

    def __calcDistance(self, location1: Location, location2: Location) -> float:
        # Eucleidean distance formula
        return sqrt(
            (location1.get_latitude() - location2.get_latitude()) ** 2
            + (location1.get_longitude() - location2.get_longitude()) ** 2
        )

    def __calcFare(self, vehicle: Vehicle, distance: float):
        if vehicle.type == "Car":
            return distance * 20
        elif vehicle.type == " Bike":
            return distance * 12
        else:
            return distance * 8

    def bookRide(self, passenger: Passenger, distance: float):
        # Edge case
        if len(self.drivers) == 0:
            print(f"No drivers available for {passenger.name}")
            return
        # Hard coded logic assignemnt
        # Find the nearest driver
        # O(n) - Brute Force
        assignedDriver = None
        minDistance = float("inf")
        for driver in self.drivers:
            currentDriverDistance = self.__calcDistance(
                passenger.location, driver.location
            )
            if currentDriverDistance < minDistance:
                minDistance = currentDriverDistance
                assignedDriver = driver

        # Fare Calculate
        expectedFare: float = self.__calcFare(assignedDriver.vehicle, distance) 

        # Check if the driver is ASSIGNED/AVAILABLE

        # Show the driver and fare to the passenger
        print(
            f"Ride booked for {passenger.name} with driver {assignedDriver.name} with fare of Rs.{expectedFare}"
        )
        print(f"Driver is on the way and is {minDistance:.2f}km away")
