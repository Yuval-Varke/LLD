from discount_strategy import DiscountStrategy

class DiscountService:
    def __init__(self,discount_strategy:DiscountStrategy):
        self.__strategy = discount_strategy

    def set_strategy(self,new_strategy:DiscountStrategy):
        self.__strategy = new_strategy

    def process(self):
        self.__strategy.calculate_discount()