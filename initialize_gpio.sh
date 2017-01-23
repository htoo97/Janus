#!/bin/bash

#to initialize gpio ports
sudo su

#replace <OUTPUT_PIN> with the gpio port you choose for output to send signal 
#from DragonBoard to Arduino
sudo <OUTPUT_PIN> > /sys/class/gpio/export
sudo out > /sys/class/gpio/gpio<OUTPUT_PIN>/direction
sudo 0 > /sys/class/gpio/gpio<OUTPUT_PIN>/value

#replace <INPUT_PIN> with the gpio port you choose for input to receive signal
#from Arduino to DragonBoard
sudo <INPUT_PIN> > /sys/class/gpio/export
sudo in > /sys/class/gpio/gpio<INPUT_PIN>/direction
