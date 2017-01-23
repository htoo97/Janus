#!/bin/bash

while :
do
  # replace <INPUT_PIN> with gpio pin you assigned for input earlier
  force=$( sudo cat /sys/class/gpio/gpio<INPUT_PIN>/value )]
  echo $force
#  if [ $force -eq 1 ]
#    sudo python detect_face.py haarcascade_frontalface_alt2.xml
#    wait
#  fi
done
