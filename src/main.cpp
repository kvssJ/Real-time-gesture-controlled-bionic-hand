#include <Arduino.h>
#include <Servo.h>

int potpin = A3;  // analog pin used to connect the potentiometer
int val;    // variable to read the value from the analog pin
Servo thumb;
Servo index;
Servo middle;
Servo ring;
Servo pinky;

// serial communication distance inputs

int inputThumb;
int inputIndex;
int inputMiddle;
int inputRing;
int inputPinky;

// angle output to servos 

int angleThumb;
int angleIndex;
int angleMiddle;
int angleRing;
int anglePinky;

int testAngle = 180;

void setup() {
   Serial.begin(9600); 
   middle.attach(9);
   thumb.attach(7);
   ring.attach(10);
   index.attach(8);
   pinky.attach(11);
  
}


void loop() {
  


// scale it for use with the servo (value between 0 and 180)


  

if(Serial.available()){
    String distanceValues = Serial.readStringUntil('\n');
   
    inputThumb = distanceValues.substring(0, distanceValues.indexOf(',')).toInt();
    distanceValues = distanceValues.substring(distanceValues.indexOf(',') + 1);

    inputIndex = distanceValues.substring(0, distanceValues.indexOf(',')).toInt();
    distanceValues = distanceValues.substring(distanceValues.indexOf(',') + 1);

    inputMiddle = distanceValues.substring(0, distanceValues.indexOf(',')).toInt();
    distanceValues = distanceValues.substring(distanceValues.indexOf(',') + 1);

    inputRing = distanceValues.substring(0, distanceValues.indexOf(',')).toInt();
    distanceValues = distanceValues.substring(distanceValues.indexOf(',') + 1);

    inputPinky = distanceValues.toInt();

    angleThumb = map(inputThumb, 120 , 20 ,0, 180);
    angleIndex = map(inputIndex, 55 , 160 ,0, 180);
    angleMiddle = map(inputMiddle, 40 , 170  ,0, 180);
    angleRing = map(inputRing, 40 , 140 ,0, 180);
    anglePinky = map(inputPinky,10 , 140 ,0, 180);


    thumb.write(angleThumb);
    index.write(angleIndex);
    middle.write(angleMiddle);
    ring.write(angleRing);
    pinky.write(anglePinky);


  
    
  }
 
                           
}
