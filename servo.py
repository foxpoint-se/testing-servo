import time
from gpiozero import Servo
from gpiozero.pins.mock import MockFactory, MockPWMPin


from gpiozero.pins.pigpio import PiGPIOFactory

# from gpiozero.pins.native import NativeFactory

SERVO_PIN = 12

factory = PiGPIOFactory()
# factory = NativeFactory()
# factory = MockFactory()
# factory = MockFactory(pin_class=MockPWMPin)

servo = Servo(
    SERVO_PIN,
    pin_factory=factory,
    # min_pulse_width=0.81 / 1000, max_pulse_width=2.2 / 1000
)


print("start in the middle")
# servo.value = 0
servo.mid()
time.sleep(3)
print("go to min")
servo.min()
# servo.value = -1
time.sleep(3)
print("go to max")
# servo.value = 1
servo.max()
time.sleep(3)
print("back to middle")
# servo.value = 0
servo.mid()
time.sleep(3)
