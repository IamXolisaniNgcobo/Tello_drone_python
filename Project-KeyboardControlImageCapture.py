from djitellopy import tello
import keyPressModule as kp
import time
import cv2

kp.init()

drone = tello.Tello()
drone.connect()
print(drone.get_battery() + " percent")
global drone_image

drone.streamon()

def get_keyboard_input():
    left_right, forward_backward, up_down, yo_velocity = 0, 0, 0, 0
    speed = 50
    # Left- Right movement
    if kp.getKey('LEFT'):
        left_right = -speed  # left control
    elif kp.getKey('RIGHT'):
        left_right = speed  # right control

    # Up - Down Movement
    elif kp.getKey('w'):
        up_down = speed  # up control
    elif kp.getKey('s'):
        up_down = -speed  # down control

    # Forward - Backward
    if kp.getKey('UP'):
        forward_backward = speed  # forward control
    elif kp.getKey('DOWN'):
        forward_backward = -speed  # backward control
    # Yo Velocity
    if kp.getKey('a'):
        yo_velocity = speed  # clockwise control
    elif kp.getKey('d'):
        yo_velocity = -speed  # anticlockwise control

    # drone takeoff
    if kp.getKey('e'):
        drone.takeoff()

    # drone land
    if kp.getKey('x'):
        drone.land()

    if kp.getKey('z'):
        cv2.imwrite(f'Resources/Images/{time.time()}.jpg', drone_image)
        time.sleep(0.3)

    return [left_right, forward_backward, up_down, yo_velocity]


while True:
    rc_control_values = get_keyboard_input()
    drone.send_rc_control(rc_control_values[0], rc_control_values[1], rc_control_values[2], rc_control_values[3])
    drone_image = drone.get_frame_read().frame
    drone_image = cv2.resize(drone_image, (360, 240))
    cv2.imshow("Live Drone Image", drone_image)
    cv2.waitKey(1)
