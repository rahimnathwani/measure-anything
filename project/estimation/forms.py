from flask.ext.wtf import Form
from wtforms import DecimalField, StringField, SubmitField, HiddenField
from wtforms.validators import Required

class EstimateForm(Form):
	question_id = HiddenField('Question ID', validators=[Required()])
	low = DecimalField('Low estimate', validators=[Required()])
	high = DecimalField('High estimate', validators=[Required()])
	submit = SubmitField("I'm 90% sure the answer is between these values")
