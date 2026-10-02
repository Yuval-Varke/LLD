from abc import ABC, abstractmethod

class Beverage:
    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod    
    def get_cost(self) -> int:
        pass    


class Coffee(Beverage):
    def get_description(self) -> str:
        return "Plain Coffee"
    def get_cost(self) -> int:
        return 20


class AddOnDecorator(Beverage):
    def __init__(self,coffee:Coffee):
        self._coffee = coffee

    def get_description(self):
        pass

    def get_cost(self):
        pass

class MilkDecorator(AddOnDecorator):
    def get_description(self):
        return self._coffee.get_description() + " with Milk"
    def get_cost(self):
        return self._coffee.get_cost() + 20


class WhipCreamDecorator(AddOnDecorator):
    def get_description(self):
        return self._coffee.get_description() + " with Whip Cream"
    def get_cost(self):
        return self._coffee.get_cost() + 50


class SugarDecorator(AddOnDecorator):
    def get_description(self):
        return self._coffee.get_description() + " with Sugar"
    def get_cost(self):
        return self._coffee.get_cost() + 5




coffee = Coffee()

milk_coffee = MilkDecorator(coffee)
print(milk_coffee.get_description())
print(milk_coffee.get_cost())

whipcream_coffee = WhipCreamDecorator(coffee)
print(whipcream_coffee.get_description())
print(whipcream_coffee.get_cost())

sugar_coffee = SugarDecorator(coffee)
print(sugar_coffee.get_description())
print(sugar_coffee.get_cost())