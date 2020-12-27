# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 20:44:57 2020

@author: Admin
"""


from tensorflow.keras.applications import VGG16
from tensorflow.keras.preprocessing import image
import pandas as pd 
import cv2
import numpy as np
from emotion_model import model
import random

EMOTION_DICT = {1:"neutral", 2:"angry", 3:"happy", 4:"sad", 5:"surprise", 6:"fear", 7:"disgust"}
model_VGG = VGG16(weights='imagenet', include_top=False)

df = pd.read_csv(r"Final_recommendations_for_emotion_project.csv")
df_new = df[['title','emotion']]
df_new = pd.DataFrame(df_new)

model = model()
model.load_weights(r"vgg_weights_updated_2_tensor.h5")

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


def give_prediction(basepath):
    text = return_prediction(basepath)
    if(text == 'happy' or text == 'sad' or text == 'angry'):
            emo_list = df_new[df_new['emotion']  == text]
            emo_list = emo_list['title'].tolist()
            sampling_1 = random.choices(emo_list, k=4)
            with open('./recom_file.txt','w') as file:
                for i in sampling_1:
                    file.write('%s\n' % i)