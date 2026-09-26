from order import Order
from chef import Chef

class PizzaOrder(Order):
    def __init__(self,chef:Chef):
        self.__chef = chef

    def execute(self):
        print("Pizza Order !")
        self.__chef.cook_burger()