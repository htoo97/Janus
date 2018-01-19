# Janus
### Face-detecting door system triggered by doormat
-- Authored by Team "What the Hack" during H.A.R.D. Hack (Hackathon) at UC San Diego (with Wayne Li, Kamran Aladross, Daniel Truong, Ash Zafari and Thant Htoo Zaw), and won 3rd place.

Find us on [Qualcomm's developer site](https://developer.qualcomm.com/project/janus-roman-god-doors)!

(**Trivia**: Janus is the Roman god of *doors*, with two *faces*.)

Summary:
--------
The theme of this hackathon was "smart home". In lieu with the theme, we built a door that requires no keys, no pin codes, no magnetic strips, nothing physical - the user just needs a phone number with at least sms capabilities (preferrably mms too). 
The unassuming welcome mat at the door is the next door bell. It is armed with a force resistor that has been tuned in Arduino so that a person of at least 25 kg/55 pounds equivalent to that of a kid will trigger the face-detecting camera. The user will not be aware of it, as the camera does the peeping for you and searches for faces. When it detects one, it sends the user a photo of the scene with the face highlighed and asks if the user wants to unlock the door for the guest. If the user texts `unlock`, the door will unlock and let the guest in. It will lock back whenever the door is closed again due to the flex sensor installed at the hinge. 

This project was built with backward compatibility as well as availability in mind as we move forward. Multiple phone numbers can be notified, and potentially issue the `unlock` command too if you buy Twilio's non-trial phone number. Any phone with sms capability can send the 'unlock' code to unlock the door, so even my grandpa who still prefers feature phones is still in control. Control the door from your bed with Janus.

Hardware: 
---------
*DragonBoard 410c* with Power Supply  
*Arduino Uno* with USB cable to power   
web camera (USB)  
servo motor  
force resistor  
flex sensor  
wiring (breadboard & jumper wires)  
microSD card (for setting up the OS of *DragonBoard*)  

**PREVIEW**
![Front](http://i.imgur.com/MhffDqU.jpg) ![Inside look at servo motor lock](http://i.imgur.com/JZBUXkd.jpg =10x10) ![DragonBoard behind the scene](http://i.imgur.com/dnaatbW.jpg =10x10)
Software:
---------
1. [Set up your *DragonBoard* with Debian.](https://github.com/96boards/documentation/wiki/Dragonboard-410c-Installation-Guide-for-Linux-and-Android#install-android-or-debian-from-an-sd-card)

2. Refresh your repositories.
  ```bash 
  sudo apt-get update -y
  sudo apt-get upgrade -y
  ```

3. Download the repository as a zip and extract it. Go the extracted folder.

4. Download all the necessary software packages and libraries, including any text editor.
  ```bash
  mkdir janus 
  cd janus
  sudo apt-get vim
  sudo apt-get install python
  sudo apt-get install pyton-opencv
  sudo apt-get install pip
  sudo pip install twilio
  sudo pip install flask
  ```

5. Download [ngrok](https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip). Unzip it using `unzip ngrok-stable-linux-arm.zip`.

6. Choose your port numbers and edit the file to initialize your gpio input and output ports. Run the script after editing.
  ```bash
  vim initialize_gpio.sh
  ./initialize_gpio.sh
  ```

7. Register for a [Twilio](https://www.twilio.com/) account, and set up a free phone number. 

8. Change account_sid, auth_token, RECEIVING_PHONE and TWILIO_NUMBER in `send_sms.py` file to match those in your Twilio account. 
  ```bash
  vim send_sms.py
  ```

9. Type the following line to activate `ngrok` tunneling at port `5000` in a new terminal. Note down the web address ending in `.io` on the 5th line beside forwarding. Keep this window open.
  ```bash
  xterm -e ./ngrok http 5000
  ```
  
10. Go to Twilio and navigate to your chose phone number's settings. Paste the web address from ngrok above appended with a `/sms' at the end.
  ![Twilio webhook](http://i.imgur.com/eZoWcAY.jpg)

11. Run the `respond_sms.py` script that enable receving commands via sms. It will open up a new terminal. Keep it open.
  ```bash
  xterm -e python respond_sms.py
  ```

12. Change the permissions so that all scripts are enabled to read, write and execute.
  ```bash
  ./change_permissions.sh
  ```

13. Enter email credentials and your phone number (near the end of the file) into the face detection script.
  ```bash
  vim detect_face.py
  ```

14. *(Optional)* Conceptually, this should be the end step. Activating the force sensor runs the detect_face.py script. However, we ran into OpenCV issues integrating the python script into bash script, or the python script into another python script with subprocess bash call. However, if you want to test out the force resistor (our door mat), run the script `xterm -e ./activate_janus.sh` and it will print in a new terminal the signal received from the force resistor through Arduino. If you want, you can try out the concept by deleting the '#' signs to uncomment the if conditional line in the shell script.

15. Manually start the face detection script. 
  ```bash
  python detect_face.py haarcascade_frontalface_alt2.xml
  ```
  The camera will load up. 
  
16. When it finds a face, it sends a multimedia message from your email to your phone, as well as a sms notifying the user that a guest is at the door and asking for a reply. Replying `unlock` to the sms will unlock the door. It has to be opened within 3 seconds of unlocking. After opening the door, it will stay unlocked until it has been closed back, ensured by the flex sensor.

17. Congratulations! **Janus** now serves you.
