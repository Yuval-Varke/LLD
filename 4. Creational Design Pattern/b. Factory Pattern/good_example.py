from abc import ABC, abstractmethod


class Food(ABC):
    @abstractmethod
    def prepare(self):
        pass


class Pizza:
    def prepare(self):
        print("Preparing pizza")


class Burger:
    def prepare(self):
        print("Preparing burger")


class Pasta:
    def prepare(self):
        print("Preparing burger")


class FoodFactory:
    @staticmethod
    def create_food(food_type: str) -> Food:
        if food_type == "pizza":
            return Pizza() # type: ignore
        elif food_type == "burger":
            return Burger() # type: ignore
        elif food_type == "pasta":
            return Pasta() # type: ignore
        else:
            return None # type: ignore


class RestrauntService:
    def create_order(self, food_type: str):
        f = FoodFactory.create_food(food_type)
        if f is None:
            print("Cannot prepare food")
            return None
        f.prepare()
        return f


restraunt_service = RestrauntService()
restraunt_service.create_order("pizza")
restraunt_service.create_order("burger")
restraunt_service.create_order("pasta")