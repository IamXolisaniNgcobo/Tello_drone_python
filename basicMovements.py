from djitellopy import tello
from time import sleep

drone = tello.Tello()
drone.connect()
percentage_sign = chr(37)
print("Battery Status: " + drone.get_battery() + "" + percentage_sign)

drone.takeoff()
drone.send_rc_control(0, 50, 0, 0)
sleep(2)
drone.send_rc_control(0, 0, 0, 30)
sleep(2)
drone.send_rc_control(0, 0, 0, 0)
drone.land()



