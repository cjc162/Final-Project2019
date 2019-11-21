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

#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(app.root_path, 'SouthO.db')
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

app.config.from_object(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.cli.command('initdb')
def initdb_command():
	db.create_all()

	f = open("static/images.csv", "r")

	for line in f:
		images = [x.strip() for x in line.split(',')]

		if (len(images) != 4):
			continue

		db.session.add(Images(images[0], images[1], images[2], images[3]))
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

@app.route('/gallery', methods=['GET', 'POST'])
def gallery():
	error = None

	if request.method == 'POST':
		if (request.form['filter'] == "all"):
			images = Images.query.all()
		else:
			images = Images.query.filter_by(category=request.form['filter']).all()
	else:
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
