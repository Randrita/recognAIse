from flask import Flask, app, render_template, request, flash ,session,send_file
import csv
import os
import pytesseract
import cv2
import numpy as np


#import urllib.urlopen
from urllib.request import urlopen
from json import load
import json
import requests

app = Flask(__name__)


@app.route('/')
def index():
   return render_template('index.html')

@app.route('/second.html' ,methods=['GET','POST'])
def second():
   return render_template('second.html')




if __name__=="__main__":
    app.run(debug=True)


