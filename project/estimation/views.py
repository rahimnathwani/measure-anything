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
@estimation.route('/results', methods=['GET'])
@login_required
def results():
    estimates = current_user.estimates
    answers = [(estimate.lowerbound, estimate.upperbound, Question.query.get(estimate.question_id).answer, Question.query.get(estimate.question_id).text) for estimate in estimates]
    scores = [1 if answer[0] <= answer[2] <= answer[1] else 0 for answer in answers]
    lifetime_accuracy = int(100 * sum(scores) / len(scores))
    return render_template('results.html', lifetime_accuracy = lifetime_accuracy, answers = answers, scores = scores)

