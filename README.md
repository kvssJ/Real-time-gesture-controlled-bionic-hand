# Real-time-gesture-controlled-bionic-hand
A model of a bionic hand that tracks and mimics real time hand movements using a hand landmarks with a webcam.

<img width="480" height="696" alt="image" src="https://github.com/user-attachments/assets/049817f5-1855-4ebf-9459-99a2d4002eef" />



# The software

The project uses the popular mediapipe handlandmarker task to track hand movements. The task uses an AI model that tracks 21 landmarks on a person's hand in real time and returns the coordinates of the landmarks either in the world coordinates or the image coordinates. It is highly accurate and works well even for faster hand motion. 

<img width="1107" height="410" alt="image" src="https://github.com/user-attachments/assets/fc2cffc9-a484-4745-bb56-5f69af3d2d58" />



I was thinking of tracking the distances between the apex of each finger and the wrist. When I bend a finger, this distance would decrease and I can turn a servo a relevant amount based on this distance. As you can see below, I used the distance formula to measure these distances between the apex of each finger and the wrist.

```     
      distanceMiddle = int(math.sqrt((wristX - middleX)**2 + (wristY-middleY)**2))
      distanceRing = int(math.sqrt((wristX - ringX)**2 + (wristY-ringY)**2))
      distanceIndex = int(math.sqrt((wristX - indexX)**2 + (wristY-indexY)**2))
      distancePinky = int(math.sqrt((wristX - pinkyX)**2 + (wristY-pinkyY)**2))
      distanceThumb = int(math.sqrt((thumb2X - thumbX)**2 + (thumb2Y-thumbY)**2)
```

Since I wanted to use the landmarker task with my webcam, I used the opencv library in python to use access my webcam and get the relevant data. I created a python program to store the distance values in variables and concatenate them into a single string. I used pyserial to send this string over serial communication to my arduino nano. Using a bit of string handling, I used a C++ program to splice the string and store the relevant data in variables. The library I used to control the servos required an input of a number from 0-180 to turn it a certain number of degrees. I used the arduino map() function to convert the distances into a value between 0 and 180 and control the servos. This worked well.

```
    angleThumb = map(inputThumb, 120 , 20 ,0, 180);
    angleIndex = map(inputIndex, 55 , 160 ,0, 180);
    angleMiddle = map(inputMiddle, 40 , 170  ,0, 180);
    angleRing = map(inputRing, 40 , 140 ,0, 180);
    anglePinky = map(inputPinky,10 , 140 ,0, 180);   
```

# The actual hand

I unfortunately had no access to a 3D printer to print a good model with faster and better actuation mechanics. Since I was more focused on just implementing the idea or building a model of the robotic hand, I took help from a friend in making a cardboard model of a robotic hand. The hand itself took no money to build. As you can see in the pictures below, the hand itself was made from cardboard. Regular strings were used with the joints and the channels to connect the strings to the cardboard were made out of of old pens. It was a REALLY cheap model. I also added springs from old click pens on the other side of the hand to straighten the hand out when relaxed. 

The only expensive part were the servos. I used five hobby servos to control the strings. 

# Power supply

The easiest way to power hobby servos is using the microcontroller but the power supply from a microcontroller is too little for five servos and the servos might even draw too much current and damage the microcontroller. Instead, I powered all five servos with a high power output battery eliminator. However, even my battery eliminator had a current output too little for the five servos. I fixed this by using a buck converter. 

<img width="300" height="300" alt="image" src="https://github.com/user-attachments/assets/ec5a7762-b3d9-4c06-bb95-3d5f14afbfbf" />



A buck converter can be used to convert a high voltage to a smaller voltage, while keeping the power output the same as the input. I increased the voltage output of the battery eliminator to 14V and adjusted the buck converter to output 5V. To keep the power the same, the buck converter increases the current output. This was sufficient for the five servos. 

# Future plans

In the future, I hope to 3D print the hand and transfer all the electronics to the 3D printed hand. I also hope to experiment with better and newer actuation methods. I think it'll be pretty fun to add the option to play games like rock, paper, scissors or hand cricket with the hand. There are so many ways to improve the existing model as well. 
