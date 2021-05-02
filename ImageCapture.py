from djitellopy import tello
import cv2

drone = tello.Tello()
drone.connect()
percentage_sign = chr(37)
print(drone.get_battery(), percentage_sign)

drone.streamon()

while True:
    drone_image = drone.get_frame_read().frame
    # drone_image = cv2.resize(drone_image(360, 240))
    cv2.imshow("Live Drone Image", drone_image)
    cv2.waitKey(1)
