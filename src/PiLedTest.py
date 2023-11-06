import RPi.GPIO as GPIO #import RPi.GPIO module
import time
from time import sleep

from hal import hal_led as led
from hal import hal_input_switch as switch

def main():
    led.init()
    switch.init()

    ret = switch.read_slide_switch()

    if ret == 1:
        led.blink_led(0.1)
    else:
        led.blink_led(0.05)


# Main entry point
if __name__ == "__main__":
    main()


