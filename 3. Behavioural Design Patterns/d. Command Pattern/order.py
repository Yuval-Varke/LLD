from abc import ABC, abstractmethod
from chef import Chef

class Order:
    @abstractmethod
    def execute(self):
        pass