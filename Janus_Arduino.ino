/*declare pin*/
#include <Servo.h>
int force = A0;
int level;
//we will change LED to UNLOCKo
int dragUnlock = A2 ;
int x;
int unlock;
int mat = 12;
int flex = A1;
Servo myservo;

void setup() {
  pinMode(force, INPUT);
  pinMode(dragUnlock, INPUT);
  pinMode(flex, INPUT);
  myservo.attach(9);
  Serial.begin(9600);
}

void loop() {
  level = analogRead(force);
  Serial.println(level);
  if (level >= 500)
  {
    digitalWrite(mat, HIGH);
    delay(1500);
    digitalWrite(mat, LOW);
  }
  unlock = analogRead(dragUnlock);
  //x = map(level,0,150,0,250);
  //Serial.println(level);
  if (unlock >= 300)
  { //UNlock code
    myservo.writeMicroseconds(500);
    //digitalWrite(level2,1);
  }
  delay(1000);
  int flexed = analogRead(flex);
  Serial.println(flexed);
  if (flexed <= 50)
  { //LOCK CODE
    delay(2000);
    myservo.writeMicroseconds(1500);
  }
  // else
  // { //LOCK CODE
  //   myservo.writeMicroseconds(1500);
  //}
}
