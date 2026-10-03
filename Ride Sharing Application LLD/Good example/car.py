from vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, number_plate):
        super().__init__(number_plate)

    def get_fare_amount(self):
        return 20