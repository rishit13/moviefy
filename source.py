# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
from prediction_utils import rerun




def capture():
    cap = cv2.VideoCapture(0)
    rerun("None", cap)
    
    
