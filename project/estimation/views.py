from flask import render_template, request
from flask.ext.security import login_required
from . import estimation
from .models import Question
from .forms import EstimateForm
import random

def get_random_question():
	return random.choice(Question.query.all())

@estimation.route('/')
def index():
	return render_template('index.html')

@estimation.route('/question', methods=["POST", "GET"])
@login_required
def questionform():
	question = get_random_question()
	form = EstimateForm(request.values, question_id=question.id)
	if request.method == 'POST' and form.validate():
		return str(form.data)
	return render_template('question.html', form = form, question = question.text)

