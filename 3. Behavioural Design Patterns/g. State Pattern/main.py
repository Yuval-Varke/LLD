from transport_service import TransportService
from bike import BikeMode
from walking import WalkingMode

bike = BikeMode()
walk = WalkingMode()

ts = TransportService(bike)
ts.eta()
ts.directions()

print("-----------------")

ts = TransportService(walk)
ts.eta()
ts.directions()