#!/usr/bin/python

# add this at end of /etc/rc.local
#
## LED blinking
##/usr/bin/nohup /usr/bin/python /home/pi/blinken/blink.py > /tmp/blink.log 2>&1 &
#

import RPi.GPIO as GPIO
import time
from mpd import MPDClient

# -----------------------------------------
def main():

    GPIO.setwarnings(False)

    # wait until MPD is ready
    client = MPDClient()
    client.timeout = 10
    while True:
        try:
            client.connect("localhost", 6600)
            break
        except:
            pass
        # quick blinks
        led_set(24, 'on')
        time.sleep(0.1)
        led_set(24, 'off')
        time.sleep(1)

    # now MPD is running
    led_set(24, 'on')

    led_switch_time = 1.7
    led_state = 'off'

    # Loop to blink our led
    while True:

        current_state = client.status()
        if current_state['state'] == 'play':

            # change led state
            if led_state == 'off':
                led_set(23, 'on')
                led_state = 'on'
            else:
                led_set(23, 'off')
                led_state = 'off'

        else:

            led_set(23, 'off')

        time.sleep(led_switch_time)



# -----------------------------------------
# LED control.
# number = 23 (103 T) or 24 (ON)
# state = on or off

def led_set(number, state):

    GPIO.setmode(GPIO.BCM)

    # Set up the GPIO pin for output
    possible_leds = [23, 24]
    if number not in possible_leds:
        print "wrong led number, please use %s" % possible_leds

    # inverted logic, the LED are cabled to + amd the gpio pulls down
    if state == 'on':
        GPIO.setup(number, GPIO.OUT)
        GPIO.output(number, GPIO.LOW)
    elif state == 'off':
        GPIO.setup(number, GPIO.OUT)
        GPIO.output(number, GPIO.HIGH)
    else:
        print "wrong state, use 'on' or 'off'"


# ------------------------------------------------------------------------
if __name__ == '__main__':
    main()
