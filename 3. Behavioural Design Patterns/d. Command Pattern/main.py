from chef import Chef
from pizza_order import PizzaOrder
from burger_order import BurgerOrder
from waiter import Waiter

chef = Chef()
burgerOrder = BurgerOrder(chef)
pizzaOrder = PizzaOrder(chef)

waiter = Waiter()

waiter.take_order(burgerOrder)
print("-----------------------")
waiter.take_order(pizzaOrder)