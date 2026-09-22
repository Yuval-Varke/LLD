class Animal:
    gender = "Male"                        #class attribute
    def __init__(self,name,age):           
        self.name = name                   #instance attribute
        self.age = age                     
    def info(self,user):                   #instance method
        print(f"This is a lion - {user}")

    @classmethod                           #class method
    def clmethod(cls):
        print(f"{cls.gender}: this is a Class method")
    
    @staticmethod                          #static method
    def greet():
        print("Hello, I am a static method")


obj = Animal("Yuval",32)
# obj.info("Yuval")
# obj.clmethod()
obj.greet()