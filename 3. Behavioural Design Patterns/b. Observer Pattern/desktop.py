from observer import Observer

class DesktopDisplay(Observer):
    def update(self,temp):
        print(f"Desktop: Temperature updated to {temp}")