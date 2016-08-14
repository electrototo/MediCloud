#include <SoftwareSerial.h>

SoftwareSerial xbee(2, 3);

byte MOTOR_PIN = 8;
byte BUZZER = 9;

char message;

boolean now = false;

unsigned long previousMillis;
long interval = 1000;

boolean alertOn = false;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  xbee.begin(9600);

  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:

  if(xbee.available()!=0){
    message = xbee.read();
    Serial.println(message);
  }

  switch(message){
    case 'a':
      //time to take a pill
      now = true;
      break;
  }

  if((millis() - previousMillis >= interval) && now){
    previousMillis = millis();
    
    if(!alertOn){
      digitalWrite(BUZZER, HIGH);
      digitalWrite(MOTOR_PIN, HIGH);

      alertOn = true;
    } else {
      digitalWrite(BUZZER, LOW);
      digitalWrite(MOTOR_PIN, LOW);

      alertOn = false;
    }
  }
}

