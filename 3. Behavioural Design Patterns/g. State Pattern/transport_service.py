from transport_mode import TransportMode

class TransportService(TransportMode):
    def __init__(self, mode: TransportMode):
        self.__mode: TransportMode = mode

    def set_mode(self,new_mode:TransportMode):
        self.__mode: TransportMode = new_mode

    def eta(self):
        self.__mode.eta()

    def directions(self):
        self.__mode.directions()