# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 18:26:48 2020

@author: Admin
"""
from __future__ import division, print_function
import os
import sys
import glob
from flask import Flask, render_template, request, redirect,url_for
from source_1 import capture_1
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods = ['GET', 'POST'])

def recommend():
    filename = request.form["file_name"]
    filepath = "./uploads/"+ filename
    recommendations =  capture_1(filepath)
    return render_template('index.html', predictions_text = recommendations)
if __name__ == '__main__':
     app.run(debug = True)
