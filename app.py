from flask import Flask, render_template, request
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import DecimalField, StringField, SubmitField, HiddenField
from wtforms.validators import Required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'any string which is not guessable'
manager = Manager(app)
bootstrap = Bootstrap(app)

class EstimateForm(Form):
	question_id = HiddenField('Question ID', validators=[Required()])
	low = DecimalField('Low estimate', validators=[Required()])
	high = DecimalField('High estimate', validators=[Required()])
	submit = SubmitField("I'm 90% sure the answer is between these values")

class Question:
	def __init__(self, id, text, answer):
		self.id = id
		self.text = text
		self.answer = answer

def get_random_question():
	return Question(1, "How tall is the empire state building, in metres?", 381)

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