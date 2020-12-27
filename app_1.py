# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 18:26:48 2020

@author: Admin
"""

import os
from flask import Flask, render_template, request, redirect,url_for
from source_1 import capture_1
app_1 = Flask(__name__)


@app_1.route('/')
def home():
    return render_template('index.html')

@app_1.route('/recommend', methods = ['GET', 'POST'])

def recommend():
    filename = request.form["file_name"]
    filepath = "./uploads/"+ filename
    recommendations =  capture_1(filepath)
    return render_template('index.html', predictions_text = recommendations)
if __name__ == '__main__':
     app_1.run(debug = True)
