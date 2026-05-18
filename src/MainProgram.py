#@markdown We implemented some functions to visualize the hand landmark detection results. <br/> Run the following cell to activate the functions.
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import cv2
import numpy as np
import math
import serial
import time

#for python to arduino serial communication

nano = serial.Serial(port = 'COM3', baudrate = 9600, timeout = 1)
time.sleep(2)

timePrev = 0


# handlandmarker object

base_options = python.BaseOptions(model_asset_path=r"C:\Users\kvsiv\OneDrive\Desktop\hand_landmarker.task")
options = vision.HandLandmarkerOptions(base_options=base_options,
                                       num_hands=2)
detector = vision.HandLandmarker.create_from_options(options)

#objects to visualise hand shit

mp_hands = mp.tasks.vision.HandLandmarksConnections
mp_drawing = mp.tasks.vision.drawing_utils
mp_drawing_styles = mp.tasks.vision.drawing_styles

#variables

MARGIN = 10  # pixels
FONT_SIZE = 1
FONT_THICKNESS = 1
HANDEDNESS_TEXT_COLOR = (88, 205, 54) # vibrant green
def draw_landmarks_on_image(rgb_image, detection_result):
  hand_landmarks_list = detection_result.hand_landmarks
  handedness_list = detection_result.handedness
  annotated_image = np.copy(rgb_image)

  # Loop through the detected hands to visualize.
  for idx in range(len(hand_landmarks_list)):
    hand_landmarks = hand_landmarks_list[idx]
    handedness = handedness_list[idx]

    # Draw the hand landmarks.
    mp_drawing.draw_landmarks(
      annotated_image,
      hand_landmarks,
      mp_hands.HAND_CONNECTIONS,
      mp_drawing_styles.get_default_hand_landmarks_style(),
      mp_drawing_styles.get_default_hand_connections_style())

    # Get the top left corner of the detected hand's bounding box.
    height, width, _ = annotated_image.shape
    x_coordinates = [landmark.x for landmark in hand_landmarks]
    y_coordinates = [landmark.y for landmark in hand_landmarks]
    text_x = int(min(x_coordinates) * width)
    text_y = int(min(y_coordinates) * height) - MARGIN

    # Draw handedness (left or right hand) on the image.
    cv2.putText(annotated_image, f"{handedness[0].category_name}",
                (text_x, text_y), cv2.FONT_HERSHEY_DUPLEX,
                FONT_SIZE, HANDEDNESS_TEXT_COLOR, FONT_THICKNESS, cv2.LINE_AA)

  return annotated_image

cap = cv2.VideoCapture(0)


while True:
    success, img = cap.read()
    height, width = img.shape[:2]
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #load image
    mp_image = mp.Image(image_format = mp.ImageFormat.SRGB, data = imgRGB)
    #detect landmarks
    detection_result = detector.detect(mp_image) #detection_result is a handLandmarker object. Use it for the distance stuff

    annotated_image = draw_landmarks_on_image(mp_image.numpy_view(), detection_result)
    lander = detection_result.hand_landmarks #list storing hand landmarks
    #lander[0] is to access landmarker data for one hand, lander[1] is to access landmarker data for the other hand
    #each of this elements is a list of NormalizedLandmark objects


    if (len(lander) != 0):

      #landmarks information

      wristY = (lander[0][0].y)*height
      wristX = (lander[0][0].x)*width     
      middleY = (lander[0][12].y)*height
      middleX = (lander[0][12].x)*width
      indexY = (lander[0][8].y)*height
      indexX = (lander[0][8].x)*width
      ringY = (lander[0][16].y)*height
      ringX = (lander[0][16].x)*width
      pinkyY = (lander[0][20].y)*height
      pinkyX = (lander[0][20].x)*width
      thumbY = (lander[0][4].y)*height
      thumbX = (lander[0][4].x)*width
      thumb2Y = (lander[0][17].y)*height
      thumb2X = (lander[0][17].x)*width


      #relevant distances for all fingers

      distanceMiddle = int(math.sqrt((wristX - middleX)**2 + (wristY-middleY)**2))
      distanceRing = int(math.sqrt((wristX - ringX)**2 + (wristY-ringY)**2))
      distanceIndex = int(math.sqrt((wristX - indexX)**2 + (wristY-indexY)**2))
      distancePinky = int(math.sqrt((wristX - pinkyX)**2 + (wristY-pinkyY)**2))
      distanceThumb = int(math.sqrt((thumb2X - thumbX)**2 + (thumb2Y-thumbY)**2))

      if(time.time()-timePrev > 0.03):
        values = [distanceThumb, distanceIndex, distanceMiddle, distanceRing, distancePinky]

        distance_values = ",".join(map(str, values)) + "\n"
        nano.write(distance_values.encode())
        print(distance_values)
        timePrev = time.time()
    
    cv2.imshow("webcam image" , cv2.cvtColor(annotated_image , cv2.COLOR_BGR2RGB))
    
    cv2.waitKey(1)
    

      
      