
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, URL


class GoatForm(FlaskForm):
	name = StringField('Name', validators=[DataRequired()])
	info = TextAreaField('Info', validators=[DataRequired()])
	score = IntegerField('Score', validators=[DataRequired()])
	image_url = TextAreaField('image_url', validators=[DataRequired(), URL()])
	submit = SubmitField('Submit')
