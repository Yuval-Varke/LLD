from abc import ABC, abstractmethod

class DiscountStrategy:
    @abstractmethod
    def calculate_discount(self):
        pass

