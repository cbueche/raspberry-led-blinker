blink.py - LED control script for Raspberry music player
========================================================

I have a Raspberry Pi mounted in a solid aluminium enclosure, along with a HifiBerry DAC. The enclosure is an old Swiss PTT 64 Kbit/s copper-line modem, emptied from its original electronics. It's heavy-duty molded aluminium, providing excellent protection against RF parasites.

![Swiss PTT box](pi-box.jpg?raw=true).

I have cabled two front-end LED's of the case to GPIO channels 23 and 24, which in the case of the HifiBerry DAC seem to be unused.

The LED's are cabled in serial circuit with a small resistance to limit the current to 10 mA. Because my LED's anodes are cabled to the +5V Vcc (common-anode circuit) and had their cathode pin open, I had to invert the signal "GPIO off" means "LED on".

![LED schema](leds_schema.jpg?raw=true).


Installation
------------

I use the very nice [moodeaudio](http://moodeaudio.org/) distribution.

#### GPIO ports

```
sudo raspi-config
advanced
A6 SPI, enable, at boot
reboot
lsmod | grep spi_ (verify module is present)
```

#### GPIO modules for Python 2.7

```
sudo apt-get install python-pip
sudo pip install rpi.gpio python-mpd2
```

#### script

The blink.py script is started at end of the boot sequence by adding this line into /etc/rc.local:

```
/usr/bin/nohup /usr/bin/python /home/pi/blinken/blink.py > /tmp/blink.log 2>&1 &
```

Usage
-----

The first LED (GPIO 24) will blink until the MPD daemon has started and the script can talk to it. It will turn itself off when the shutdown initiated in the player GUI is finished.

The second LED (GPIO 23) will blink slowly when music is playing.
