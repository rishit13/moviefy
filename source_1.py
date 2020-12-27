# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 20:41:28 2020

@author: Admin
"""


from prediction_utils_1 import give_prediction

movies = []


def capture_1(basepath):
    give_prediction(basepath)
    with open('recom_file.txt', 'r') as filehandle:
        for line in filehandle:
        # remove linebreak which is the last character of the string
            currentmovie = line[:-1]
        # add item to the list
            movies.append(currentmovie)
    return movies