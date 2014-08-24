from .. import db

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(240), unique=True, index=True)
    answer = db.Column(db.Numeric)

class Estimate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))    
    lowerbound = db.Column(db.Numeric)
    upperbound = db.Column(db.Numeric)
    created_on = db.Column(db.DateTime, default=db.func.now())