from weather_station import WeatherStation
from tv import TVDisplay
from observer import Observer
from mobile import MobileDisplay
from desktop import DesktopDisplay

ws = WeatherStation()
tv = TVDisplay()

ws.add_observer(tv)
ws.update_temperature(30)

print("--------------")

mb = MobileDisplay()
ws.add_observer(mb)
ws.update_temperature(35)

print("--------------")

ws.remove_observer(mb)
ws.update_temperature(40)

print("--------------")

desk = DesktopDisplay()
ws.add_observer(desk)
ws.update_temperature(45)