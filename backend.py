from flask import Flask, app, render_template, request, flash ,session,send_file
import csv
import os
import pytesseract
import cv2
import numpy as np
import base64

#import urllib.urlopen
from urllib.request import urlopen
from json import load
import json
import requests
from pprint import pprint

from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './uploads'

app = Flask(__name__)

app.config['SECRET_KEY'] = 'gyuerho834dtrui3yr8ury39ry3yr9p834m'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
   return render_template('index.html')

@app.route('/second.html' ,methods=['GET','POST'])
def second():
   if request.method == 'POST':
         # check if the post request has the file part
         pprint(request.files)
         # pprint(request.post)
         if 'files[]' not in request.files:
               flash('No file part')
               return redirect(request.url)
         files = request.files.getlist("files[]")
         img = base64.b64encode(files[0].read()).decode()
         for file in files:
                     
            # If the user does not select a file, the browser submits an
            # empty file without a filename.
            if file.filename == '':
                  flash('No selected file')
                  return redirect(request.url)

            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
         return render_template('second.html', show=img, ext=files[0].filename.split('.')[-1])
   else:
         return render_template('second.html')
            




if __name__=="__main__":
    app.run(debug=True)


