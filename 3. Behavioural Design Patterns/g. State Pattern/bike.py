from transport_mode import TransportMode


class BikeMode(TransportMode):
    def eta(self):
        print("Bike will take 15 mins")

    def directions(self):
        print("Go left to the road")