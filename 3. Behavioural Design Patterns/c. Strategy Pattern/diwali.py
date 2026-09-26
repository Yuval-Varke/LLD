from discount_strategy import DiscountStrategy

class DiwaliStrategy(DiscountStrategy):
    def calculate_discount(self):
        print(f"Applying Diwali Discount of 20%")