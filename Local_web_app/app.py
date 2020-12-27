# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 13:16:59 2020

@author: Admin
"""


from flask import Flask, render_template
from source import capture
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index_1.html')

@app.route('/recommend', methods = ['POST'])

def recommend():
    recommendations =  capture()
    return render_template('index_1.html', predictions_text = recommendations)
if __name__ == '__main__':
     app.run(debug = True)