import os, random
from flask import Flask, render_template, request
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate, MigrateCommand
from wtforms import DecimalField, StringField, SubmitField, HiddenField
from wtforms.validators import Required

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SECRET_KEY'] = 'any string which is not guessable'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
manager = Manager(app)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

class EstimateForm(Form):
	question_id = HiddenField('Question ID', validators=[Required()])
	low = DecimalField('Low estimate', validators=[Required()])
	high = DecimalField('High estimate', validators=[Required()])
	submit = SubmitField("I'm 90% sure the answer is between these values")


class Question(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.String(240), unique=True, index=True)
	answer = db.Column(db.Numeric)

def get_random_question():
	return random.choice(Question.query.all())

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/question', methods=["POST", "GET"])
def questionform():
	question = get_random_question()
	form = EstimateForm(request.values, question_id=question.id)
	if request.method == 'POST' and form.validate():
		return str(form.data)
	return render_template('question.html', form = form, question = question.text)

if __name__ == '__main__':
	manager.run()