# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 11:55:52 2017

@author: Rishit
"""
import glob
from shutil import copyfile 
 
emotions=["neutral","anger","contempt","disgust","fear","happy","sadness","surprise"]
participants_paths=glob.glob("CK+ DATASET/*")
  
for x in participants_paths:
    serial=x[-4:]
    for sessions in glob.glob("participants_paths+Emotion/%s/*" %serial):
        for files in glob.glob("%s/*" %sessions):
         file = open(files,'r')
         current_session=files[39:-30]
         current_emotion=int(float(file.readline()))
         
         
         
         a=glob.glob("participants_paths+cohn-kanade-images/%s/%s/*"  %(serial,current_session))
         b=sorted(a)
         image_emotion_s=b[-1]
         image_neutral_s=b[0]
         
         
         neutral_d="sorted_set/neutral/%s" %image_neutral_s[42:]
         emo_d="sorted_set/ %s/%s" %(emotions[current_emotion],image_neutral_s[42:])
         
         copyfile(image_neutral_s,neutral_d)
         copyfile(image_emotion_s,emo_d)

