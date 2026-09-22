class Student:

    # Attributes

    # Methods
    def __init__(self, name:str, age: int, gender: str) -> None:
        print("This is a constructor")
        self.name = name
        self.age = age
        self.gender = gender

    def display(self) -> None:
        print(f"My name is {self.name}, age is {self.age}, and gender is {self.gender}")



s1 = Student("Yuval",22,"male")

s1.display()

