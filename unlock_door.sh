#!/bin/bash

#replace <OUTPUT_PIN> with the gpio output pin you use
sudo echo 1 > /sys/class/gpio/gpio<OUTPUT_PIN>/value
