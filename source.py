# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
from prediction_utils import rerun

places = []


def capture():
    cap = cv2.VideoCapture(0)
    rerun("None", cap)
    with open('recom_file.txt', 'r') as filehandle:
        for line in filehandle:
        # remove linebreak which is the last character of the string
            currentPlace = line[:-1]

        # add item to the list
            places.append(currentPlace)
    return places