# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 12:30:35 2020

@author: Admin
"""


import tensorflow as tf
from tensorflow.keras.regularizers import l2
input_shape = 4*4*512
def model():
    model = tf.keras.models.Sequential([ tf.keras.layers.Dense(1024, activation = 'relu',input_shape = (input_shape,)),
                                        tf.keras.layers.BatchNormalization(),
                                        tf.keras.layers.Dropout(0.2),
                                        tf.keras.layers.Dense(512, activation = 'relu', kernel_regularizer= l2(0.01)),
                                        tf.keras.layers.Dense(256, activation = 'relu', kernel_regularizer= l2(0.01)),
                                        tf.keras.layers.BatchNormalization(),
                                        tf.keras.layers.Dropout(0.2),
                                        tf.keras.layers.Dense(7, activation= 'softmax') 
    ])
    return model