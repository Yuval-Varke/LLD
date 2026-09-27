from transport_mode import TransportMode


class WalkingMode(TransportMode):
    def eta(self):
        print("Walking will take 30 mins")

    def directions(self):
        print("Go right to the road and then left")