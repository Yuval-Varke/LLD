from typing import List
from observer import Observer

class WeatherStation:
    def __init__(self):
        self.__temperature = 0
        self.__observers:List[Observer] = []

    def add_observer(self,new_observer:Observer):
        self.__observers.append(new_observer)

    def remove_observer(self,ob:Observer):
        self.__observers.remove(ob)

    def update_temperature(self,new_temp):
        self.__temperature = new_temp
        self.notify_observers()

    def notify_observers(self):
        for i in self.__observers:
            i.update(self.__temperature)