from flask import render_template, request, flash, redirect, url_for
from . import estimation
from .models import Question, Estimate
from .forms import EstimateForm
from flask.ext.login import login_required, current_user
import random
from .. import db

def create_fake_question():
    fake_question = Question(text='How tall is the Empire State Building, all the way to the tip, in metres?', answer=443)
    db.session.add(fake_question)
    db.session.commit()

def get_random_question():
    try:
        return random.choice(Question.query.all())
    except:
    	create_fake_question()
    	return get_random_question()

@estimation.route('/')
def index():
    return render_template('index.html')

@estimation.route('/question', methods=["POST", "GET"])
@login_required
def questionform():
    question = get_random_question()
    form = EstimateForm(request.values, question_id=question.id)
    if request.method == 'POST' and form.validate():
        myestimate = Estimate(user_id = current_user.id, question_id = form.question_id.data, lowerbound = form.low.data, upperbound = form.high.data)
        db.session.add(myestimate)
        db.session.commit()
        flash("OK - we've saved your answers")
        return redirect(url_for('estimation.questionform'))
    return render_template('question.html', form = form, question = question.text)

