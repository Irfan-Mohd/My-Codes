#include <Servo.h>
byte sensorPin = 0;
byte motorPin = 3;
int prev = 0;
Servo motor;

void setup() {
  // put your setup code here, to run once:
  motor.attach(motorPin);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int val = analogRead(sensorPin);
  float temp = (val/1024.0)*500;
  int delayTime = 200;
  int pos = prev;
  int des = (int)temp;
  if(pos<des){ 
   while(pos<=des){
    motor.write(pos);
    pos++;
    delay(delayTime);
   }
  }
  else{
    while(pos>=des){
      motor.write(pos);
      pos--;
      delay(delayTime);
   }
  }
  prev = des;
  delay(1000);
}
