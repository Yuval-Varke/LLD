from abc import ABC, abstractmethod


class Food(ABC):
    @abstractmethod
    def prepare(self):
        pass


class Pizza(Food):
    def prepare(self):
        print("Preparing pizza")


class Burger(Food):
    def prepare(self):
        print("Preparing burger")


# Responsible for making objects
class RestrauntService:
    def create_order(self, food_type: str):
        if food_type == "pizza":
            f = Pizza()
        elif food_type == "burger":
            f = Burger()
        else:
            print("Invalid food type")
            return None
        f.prepare()
        return f


restraunt_service = RestrauntService()
restraunt_service.create_order("pizza")
restraunt_service.create_order("burger")