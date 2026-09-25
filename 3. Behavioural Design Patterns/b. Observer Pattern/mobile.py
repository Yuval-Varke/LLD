from observer import Observer

class MobileDisplay(Observer):
    def update(self,temp):
        print(f"Mobile: Temperature updated to {temp}")