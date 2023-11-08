import RPi.GPIO as GPIO #import RPi.GPIO module
import time
from time import sleep

from hal import hal_led as led
from hal import hal_input_switch as switch

def blink_led(delay):
    led.set_output(0, 1)
    time.sleep(delay)
    led.set_output(0, 0)
    time.sleep(delay)


def main():
    led.init()
    switch.init()

    ret = switch.read_slide_switch()

    # Switch in left position -> LED blinking, 5Hz
    if ret == 1:
        while ret == 1:
            blink_led(0.1)

    else:
        # Switch in right positon -> LED blinking, 10Hz
        currentTime = time.time()
        startTime = currentTime
        while (currentTime - startTime) < 5:
            blink_led(0.05)
            currentTime = time.time()


# Main entry point
if __name__ == "__main__":
    main()


