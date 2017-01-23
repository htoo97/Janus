# Janus
### Face-detecting door system triggered by doormat
-- Authored by Team "What the Hack" during H.A.C.K. Day at UC San Diego (with Wayne Li, Kamran Aladross, Daniel Truong, Ash Zafari and Thant Htoo Zaw)

**Trivia**: Janus is the Roman god of *doors*, with two *faces*.

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

Software:
---------
1. [Set up your *DragonBoard* with Debian.](https://github.com/96boards/documentation/wiki/Dragonboard-410c-Installation-Guide-for-Linux-and-Android#install-android-or-debian-from-an-sd-card)

2. Refresh your repositories.
```bash
sudo apt-get update -y
sudo apt-get upgrade -y
```

2. Download the repository as a zip and extract it. Go the extracted folder.

3. Download all the necessary software packages and libraries, including any text editor.
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

4. Download [ngrok](https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip). Unzip it using `unzip ngrok-stable-linux-arm.zip`.

5. Choose your port numbers and edit the file to initialize your gpio input and output ports. Run the script after editing.
```bash
vim initialize_gpio.sh
./initialize_gpio.sh
```

6. 

TODONUM. Change the permissions so that all scripts are enabled to read, write and execute.
```bash
./change_permissions.sh
```

TODONUM. Start ngrok tunneling and listening to incoming messages at port: `5000` using `respond_sms.py'
```bash
./start_listening.sh
```
