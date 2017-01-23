#!/bin/bash

#replace <OUTPUT_PIN> with the gpio output pin you use
sudo echo 0 > /sys/class/gpio/gpio<OUTPUT_PIN>/value
