/*DB = DragonBoard 410C*/
#include <Servo.h>
int force = A0; //force resistor input to GPIO A0 on arduino
int level; //read value of force resistor
int dragUnlock = A2 ; //unlock code sent from DB to arduino GPIO A2
int unlock; //value that reads the high or low value of unlock code from DB
int mat = 12; //Force resistor reading output from arduino GPIO 12 to DB 
int flex = A1; //Flex resistor reading to arduino input GPIO A1 to determine if door is shut
Servo myservo; //servo motor to unlock door

void setup() {
  //assign pins on arduino of resistors
  pinMode(force, INPUT);
  pinMode(flex, INPUT);
  pinMode(dragUnlock, INPUT);  //assign DB output of unlock to arduino as input
  myservo.attach(9);   //assign servo to pin 9 of arduino
  Serial.begin(9600);
}

void loop() {
  level = analogRead(force); //reads force cable reading
  Serial.println(level); //prints continuous values of force resistor
  if (level >= 500) // if there is force being exerted on doormat
  {
    digitalWrite(mat, HIGH); //send a high value (logical 1) to DB
    delay(1500);
    digitalWrite(mat, LOW); //resets value 
  }
  unlock = analogRead(dragUnlock); //continously reads for an unlock code sent from DB
  if (unlock >= 300)
    /*300 is a value that we found was a good value for our force resistor and voltage divider combination*/
  { 
    myservo.writeMicroseconds(500); //UNLOCKS door if unlock code is sent by text message
  }
  delay(1000);
  int flexed = analogRead(flex); //Reads flex cable to see if door is closed
  Serial.println(flexed);
  if (flexed <= 50)
  { //LOCK CODE if door is closed
    delay(2000);
    myservo.writeMicroseconds(1500); //LOCKS door two seconds after the flex cable reads that door is closed
  }
}
