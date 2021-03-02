# Flask Packages
from flask import Flask,render_template,request,url_for
from flask_bootstrap import Bootstrap
from flask_uploads import UploadSet,configure_uploads,IMAGES,DATA,ALL
#from flask_sqlalchemy import SQLAlchemy

from werkzeug.utils import secure_filename
import os
import datetime
import time


# EDA Packages
#import pandas as pd
#import numpy as np

# ML Packages
#from sklearn import model_selection
#from sklearn.linear_model import LogisticRegression
#from sklearn.tree import DecisionTreeClassifier
#from sklearn.neighbors import KNeighborsClassifier
#from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
#from sklearn.naive_bayes import GaussianNB
#from sklearn.svm import SVC


# ML Packages For Vectorization of Text For Feature Extraction
#from sklearn.feature_extraction.text import CountVectorizer
#from sklearn.feature_extraction.text import TfidfVectorizer




app = Flask(__name__)
Bootstrap(app)
#db = SQLAlchemy(app)

# Configuration for File Uploads
files = UploadSet('files',ALL)
app.config['UPLOADED_FILES_DEST'] = 'static/images'
configure_uploads(app,files)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///static/uploadsDB/filestorage.db'

# Saving Data To Database Storage
#class FileContents(db.Model):
#	id = db.Column(db.Integer,primary_key=True)
#	name = db.Column(db.String(300))
#	modeldata = db.Column(db.String(300))
#	data = db.Column(db.LargeBinary)


@app.route('/')
def index():
	return render_template('index.html')

# Route for our Processing and Details Page
@app.route('/dataupload',methods=['GET','POST'])
def dataupload():
	if request.method == 'POST' and 'jpg_img' in request.files:
		file = request.files['jpg_img']
		filename = secure_filename(file.filename)
		# os.path.join is used so that paths work in every operating system
        # file.save(os.path.join("wherever","you","want",filename))
		file.save(os.path.join('static/images',filename))
		fullfile = os.path.join('static/images',filename)


		try:
			os.system('python detect_plate.py --weights weights/best_yolov5s.pt --img 2000 --conf 0.4 --source static/images/Page_112_1.jpg --plate True')
			hbr_doc = open('/static/texts/hbr.txt', 'r')
			hbr_txt = hbr_doc.read()

		except:
			hbr_txt = "This didn't work"

		# For Time
		date = str(datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d %H:%M:%S"))

	return render_template('details.html',filename=filename,date=date, hbr_txt=hbr_txt, fullfile=fullfile
		)



if __name__ == '__main__':
	app.run(debug=True)





# Jesus Saves @ JCharisTech
