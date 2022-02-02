from gpiozero import Servo
import time

SERVO_PIN = 12

servo = Servo(
    SERVO_PIN,
    # pin_factory=factory, min_pulse_width=0.81 / 1000, max_pulse_width=2.2 / 1000
)

print("hello")