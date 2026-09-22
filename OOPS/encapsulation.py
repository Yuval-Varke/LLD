# add two __ (underscores) to make any attr private 
# getter and setter methods are used to expose private attr to public


class Bank:
    def __init__(self, name: str, balance: int):
        self.name: str = name
        # Private attr
        self.__balance: int = balance

    # Getter
    def get_balance(self):
        print(f"Current balance : {self.__balance}")

    def deposit(self, amount: int):
        self.__balance += amount
        print(f"Amount deposited, current balance : {self.__balance}\n")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Not enough balance available")
        else:
            self.__balance -= amount
            print(f"Amount withdrawn, current balance : {self.__balance}\n")

acc = Bank("Yuval",1000)
acc.deposit(1000)
acc.get_balance()
acc.withdraw(500)