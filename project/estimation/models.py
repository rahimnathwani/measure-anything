from .. import db

class Question(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.String(240), unique=True, index=True)
	answer = db.Column(db.Numeric)