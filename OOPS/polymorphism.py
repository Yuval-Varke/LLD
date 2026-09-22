# Polymorphism - means same name having diff functions

# class Animal():
#     name = "lion"
#     def speak(self):
#         print("Hello, I roar")

# class Bird():
#     name = "sparrow"
#     def speak(self):
#         print("Hey, I churpp")

# a = Animal()
# b = Bird()
# a.speak()
# b.speak()


#Python does not support method overloading
#Method overriding :- 

class Animal():
    name = "lion"
    def speak(self):
        print("Hello, I roar")

class Bird(Animal):
    name = "sparrow"
    def speak(self):
        super().speak()
        print("Hey, i churpp and am an animal")

a = Bird()
a.speak()