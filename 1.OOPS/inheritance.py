class Animal:                                # parent class
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Name is {self.name} and age is {self.age}")

obj = Animal("Lion",32)
obj.display()

class Human(Animal):                          # child class
    def __init__(self, name, age, number, blood_grp):
        super().__init__(name, age)
        self.number = number
        self.blood_grp = blood_grp
    def display(self):
        print(f"Name is {self.name} and age is {self.age} and number is {self.number} and blood grp is {self.blood_grp}")

obj2 = Human("Yuval",21,2902,"AB+")
obj2.display()

class Robot(Human):
    def __init__(self, name, age, number, blood_grp, imei):
        super().__init__(name, age, number, blood_grp)

