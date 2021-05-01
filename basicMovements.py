from djitellopy import tello
from time import sleep

drone = tello.Tello()
drone.connect()
print("Battery Status: "+drone.get_battery())
print("Current WIFI: "+drone.get_wifi())
print("Current Speed: "+drone.get_speed())
print("Flight time is: "+drone.get_flight_time())