SHELL = /bin/bash

.PHONY: help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help

install-py:		## setup venv and install py dependencies
	( \
		python3 -m venv .venv; \
       	source .venv/bin/activate; \
       	python -m pip install -r requirements.txt; \
    )

install-apt:	## install apt packages
	sudo apt install python3-pip python-setuptools python3-setuptools unzip


# Stolen from https://abyz.me.uk/rpi/pigpio/download.html 
install-pigpio:		## install pigpio in this folder
	( \
		wget https://github.com/joan2937/pigpio/archive/master.zip; \
		unzip master.zip; \
		cd pigpio-master; \
		make; \
		sudo make install; \
	)

start-pigpio:		## start pigpio
	sudo pigpiod

stop-pigpio:		## stop pigpio
	sudo killall pigpiod

add-me-to-gpio:		## add current user to group `gpio`
	$(eval CURRENT_USER=$(shell whoami))
	source .venv/bin/activate
	sudo python gpio_udev_setup.py --user $(CURRENT_USER)
