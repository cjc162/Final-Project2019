from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Images(db.Model):
	img_id = db.Column(db.Integer, primary_key=True)
	path = db.Column(db.String(128), nullable=False)
	name = db.Column(db.String(64), nullable=False)
	category = db.Column(db.String(64), nullable=False)
	description = db.Column(db.String(512), nullable=False)
	
	def __init__(self, path, name, category, description):
		self.path = path
		self.name = name
		self.category = category
		self.description = description

	def __repr__(self):
		return '<Path {}>'.format(self.path)