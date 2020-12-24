# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 12:33:08 2020

@author: Admin
"""

from tensorflow.keras.applications import VGG16
from tensorflow.keras.preprocessing import image
import pandas as pd 
from GUI_utils import generate_list
import cv2
import numpy as np
from emotion_model import model


EMOTION_DICT = {1:"neutral", 2:"angry", 3:"happy", 4:"sad", 5:"surprise", 6:"fear", 7:"disgust"}
model_VGG = VGG16(weights='imagenet', include_top=False)

df = pd.read_csv(r"C:\Users\Admin\Downloads\Final_recommendations_for_emotion_project.csv")
df_new = df[['title','emotion']]
df_new = pd.DataFrame(df_new)

model = model()
model.load_weights(r"C:\Users\Admin\Downloads\vgg_weights_updated_2_tensor.h5")

def return_prediction(path):
  img = image.load_img(path, target_size=(150,150,3))
  #read_img = img_to_array(read_img)
  gray = cv2.cvtColor(np.float32(img), cv2.COLOR_BGR2GRAY)
  cv2.imwrite(path, gray)
  read_img = cv2.imread(path)
  read_img = read_img.reshape(1, read_img.shape[0], read_img.shape[1], read_img.shape[2])
  read_img.shape
  read_img = read_img/255.0
  vgg_pred = model_VGG.predict(read_img)
  vgg_pred = vgg_pred.reshape(1, vgg_pred.shape[1]*vgg_pred.shape[2]*vgg_pred.shape[3])
  y = model.predict(vgg_pred)
  y_pred = np.argmax(y, axis=1)
  y_pred = y_pred[0]
  return EMOTION_DICT[y_pred+1]


def rerun(text, cap):
  while(True):
    ret, img = cap.read()
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, "Last Emotion was "+str(text), (95,30), font, 1.0, (255, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(img, "Press SPACE: FOR EMOTION", (5,470), font, 0.4, (255, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(img, "Hold Q: To Quit", (460,470), font, 0.4, (255, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(img,"Press C to recommend movies", (5, 400), font, 0.7, (255,0,0), 2, cv2.LINE_AA)
    cv2.imshow("Image", img)

    if cv2.waitKey(1) == ord(' '):
            cv2.imwrite("test.jpg", img)
            path = r'C:\Users\Admin\Downloads\test.jpg'
            text = return_prediction(path)
            rerun(text, cap)
            break
    if cv2.waitKey(1) == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            break
    if cv2.waitKey(1) == ord('c'):
        cap.release()
        cv2.destroyAllWindows()
        if(text == 'happy' or text == 'sad' or text == 'angry'):
            generate_list(text,df_new)
        break