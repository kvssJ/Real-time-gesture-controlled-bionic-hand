# Real-time-gesture-controlled-bionic-hand
A model of a bionic hand that tracks and mimics real time hand movements using a hand landmarks with a webcam.

# Software features

The project uses the popular mediapipe handlandmarker task to track hand movements. The task uses an AI model that tracks 21 landmarks on a person's hand in real time and returns the coordinates of the landmarks either in the world coordinates or the image coordinates. It is highly accurate and works well even for faster hand motion.

# The actual hand

I unfortunately had no access to a 3D printer to print a good model with faster and better actuation mechanics. Since I was more focused on just implementing the idea or building a model of the robotic hand, I took help from a friend in making a cardboard model of a robotic hand. The hand itself took no money to build. As you can see in the pictures below, the hand itself was made from cardboard. Regular strings were used with the joints and the channels to connect the strings to the cardboard were made out of of old pens. It was a REALLY cheap model. I also added springs from old click pens on the other side of the hand to straighten the hand out when relaxed. 

The only expensive part were the servos. I used five hobby servos to control the strings. 

# Power supply

The easiest way to power hobby servos is using the microcontroller but the power supply from a microcontroller is too little for five servos and the servos might even draw too much current and damage the microcontroller. Instead, I powered all five servos with a high power output battery eliminator. However, even my battery eliminator had a current output too little for the five servos. I fixed this by using a boom converter. 

A boom converter can be used to convert a high voltage to a smaller voltage, while keeping the power constant. I increased the voltage output of the battery eliminator to 14V and adjusted the boom converter to output 5V. To keep the power the same, the boom converter increases the current output. This was sufficient for the five servos. 

# Future plans

In the future, I hope to 3D print the hand and transfer all the electronics to the 3D printed hand. I also hope to experiment with better and newer actuation methods, perhaps automated air and water pump control 
