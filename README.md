# Testing servo

Testing with the objective of getting rid of annoying jitter.

## Get started

```
git clone <this repo>
cd path/to/project
make install-apt
make install-py
make install-pigpio
make add-me-to-gpio
make start-pigpio
```

Connect a servo to ground, 5V and pwm pin 12. Then:

```
source source_me.sh
python servo.py
```

Stop pigpio if you want:

```
make stop-pigpio
```

## Notes

Is this the problem with wheel?
Seems so.
`sudo apt install python3-pip`

We definately need this. It has to do with not having this group by default on Ubuntu.
On Raspberry Pi it is already set up.
`sudo python gpio_udev_setup.py ubuntu gpio`

Could probably be good, but didn't seem to be necessary for permission problem.
`sudo apt install python-dev`


`sudo apt-get install pigpio` not working on Ubuntu.
Install using `make install-pigpio` instead.

Probably need this. At least for installing pigpio
`sudo apt install python-setuptools python3-setuptools`

And this:
`sudo apt-get install unzip`


Check here, in case of issues.
http://abyz.me.uk/rpi/pigpio/faq.html

In case of ubuntu 21.04
https://ubuntu.com/tutorials/gpio-on-raspberry-pi#1-overview
