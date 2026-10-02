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


class CoffeeWithMilk(Coffee):
    def get_description(self) -> str:
        return "Coffee with Milk"

    def get_cost(self) -> int:
        return 35



coffee = Coffee()
print(coffee.get_description())
print(coffee.get_cost())

coffee_with_milk = CoffeeWithMilk()
print(coffee_with_milk.get_description())
print(coffee_with_milk.get_cost())
