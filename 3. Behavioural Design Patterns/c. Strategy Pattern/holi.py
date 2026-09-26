from discount_strategy import DiscountStrategy

class HoliStrategy(DiscountStrategy):
    def calculate_discount(self):
        print("Applying holi discount of 10%")