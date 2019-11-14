import time
import os
from hashlib import md5
from datetime import datetime
from flask import Flask, request, session, url_for, redirect, render_template, abort, g, flash, _app_ctx_stack
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import select
from sqlalchemy.sql.functions import func

from models import db, Images

app = Flask(__name__)

SECRET_KEY = 'development key'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(app.root_path, 'SouthO.db')
#SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

app.config.from_object(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.cli.command('initdb')
def initdb_command():
	db.create_all()

	paths = {
		"test1.jpg": ["Name here", "Image description here 1"],
		"test2.jpg": ["Name here", "Image description here 2"], 
		"test3.jpg": ["Name here", "Image description here 3"], 
		"test4.jpg": ["Name here", "Image description here 4"],
		"test5.jpg": ["Name here", "Image description here 5"], 
		"test6.jpg": ["Name here", "Image description here 6"]
	}

	for path in paths:
		db.session.add(Images(path, paths[path][0], paths[path][1]))
		db.session.commit()

	print('Initialized the database.')

@app.route('/')
def index():
	images = Images.query.all()

	image_data = []
	for image in images:
		image_dict = {}

		image_dict["id"] = image.img_id
		image_dict["path"] = image.path
		image_dict["name"] = image.name
		image_dict["description"] = image.description

		image_data.append(image_dict)

	return render_template('index.html', images=image_data)

@app.route('/gallery')
def gallery():
	images = Images.query.all()

	image_data = []
	for image in images:
		image_dict = {}

		image_dict["id"] = image.img_id
		image_dict["path"] = image.path
		image_dict["name"] = image.name
		image_dict["description"] = image.description

		image_data.append(image_dict)

	return render_template('gallery.html', images=image_data)

@app.route('/img_desc/<int:id>')
def img_desc(id):
	image = Images.query.filter_by(img_id=id).first()

	return render_template('img_desc.html', image=image)
