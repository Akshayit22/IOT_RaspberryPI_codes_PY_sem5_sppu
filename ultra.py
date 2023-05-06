import RPi.GPIO as GPIO

import time
int inches= 0;
int cm = 0;
long travel_time(int triggerPin, int echoPin)
{
  pinMode(triggerPin, OUTPUT);
  pinMode(echoPin, INPUT);  
  digitalWrite(triggerPin, LOW);
  delayMicroseconds(2);
  // generate 10 Micro second pulse to trig-pin
  digitalWrite(triggerPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(triggerPin, LOW);
 
  // Reads the echo pin, and returns the sound wave travel time in microseconds
  return pulseIn(echoPin, HIGH);
}

void setup()
{
  Serial.begin(9600);

 
}

void loop()
{
 
  // distance =speed * travel_time
  cm = 0.01723 * travel_time(7, 6);
  // convert to inches by dividing by 2.54
  inches = (cm / 2.54);
  Serial.print(cm);
  Serial.print("cm, ");
  Serial.print(inches);
  Serial.println("in");
  
  delay(100); // Wait for 100 millisecond(s)
}
