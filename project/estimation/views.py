from flask import render_template, request, flash, redirect, url_for
from flask.ext.security import login_required
from flask.ext.login import current_user
from .. import db
from . import estimation
from .models import Question, Estimate
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
        myestimate = Estimate(user_id = current_user.id, question_id = form.question_id.data, lowerbound = form.low.data, upperbound = form.high.data)
        db.session.add(myestimate)
        db.session.commit()
        flash("OK - we've saved your answers")
        return redirect(url_for('estimation.questionform'))
    return render_template('question.html', form = form, question = question.text)

'''
Need to add something to:
Get current user -> estimates -> questions -> answers
'''
