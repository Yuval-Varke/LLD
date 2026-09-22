from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self,radius:int):
        self.radius = radius

    def area(self):
        print(f"Area of circle is {3.14*self.radius*self.radius}")

    def perimeter(self):
        print(f"Perimter of circle is {2*3.14*self.radius}")

c1 = Circle(1)
c1.area()
c1.perimeter()