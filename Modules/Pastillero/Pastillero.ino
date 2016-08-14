#include <SoftwareSerial.h>

#define COLS 2
#define ROWS 3
#define RED_LED 0
#define GREEN_LED   1

SoftwareSerial xbee(2, 3);

byte MOTOR_PIN = 8;
byte BUZZER = 9;

byte LEDS[ROWS][COLS] = {
  {11,10}, // First compartment
  {13,12}, // Second compartment
  {4,5}    // Third compartment
};

char message;

boolean now = false;

unsigned long previousMillis;
long interval = 1000;
int compartimiento;
boolean alertOn = false;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  xbee.begin(9600);

  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  
  for(int i = 0; i < ROWS; i++)
  {
    for(int j = 0; j < COLS; j++)
    {
      pinMode(LEDS[i][j], OUTPUT);
    }
  }
}

void loop() {
  // put your main code here, to run repeatedly:

  if(xbee.available()!=0){
    message = xbee.read();
    Serial.println(message);
  }

  switch(message){
    case '1':
      compartimiento = 1;
      now = true;
      break;
    case '2':
      compartimiento = 2;
      now = true;
      break;
    case '3':
      compartimiento = 3;
      now = true;
      break;
    case 'c':
      now = false;
      break;
    default:
      break;
  }

  if((millis() - previousMillis >= interval) && now){
    previousMillis = millis();
    
    if(!alertOn){
      // Turn on the Alarm
      //digitalWrite(MOTOR_PIN, HIGH);
      /* You need to give some time for the motor to begin running */
      //delay(120);
      //digitalWrite(BUZZER, HIGH);
      encenderCompartimiento(compartimiento);
      alertOn = true;
    } else {
      digitalWrite(MOTOR_PIN, LOW);
      digitalWrite(BUZZER, LOW);
      // Turn off all LEDs
      for(int i = 0; i < ROWS; i++)
      {
        for(int j = 0; j < COLS; j++)
        {
          digitalWrite(LEDS[i][j], LOW);
        }
      }
      alertOn = false;
    }
  }
}

void encenderCompartimiento(int c)
{
  c = c-1;
//  for(int i = 0; i < ROWS; i++)
//  {
//    digitalWrite(LEDS[i][RED_LED],HIGH);
//    delay(500);
//  }
//  
//  digitalWrite(LEDS[c][GREEN_LED], HIGH);
//  delay(500);
//  digitalWrite(LEDS[c][RED_LED], LOW);
//  delay(500);
  digitalWrite(LEDS[c][GREEN_LED],HIGH);
  delay(1000);
  digitalWrite(LEDS[c][RED_LED],HIGH);
  delay(1000);
}

