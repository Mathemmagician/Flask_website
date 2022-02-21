from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, TextAreaField, MultipleFileField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
	title = StringField('Title', validators=[DataRequired()])
	content = TextAreaField('Content', validators=[DataRequired()])
	# picture = FileField('Upload picture', validators=[FileAllowed(['jpg', 'png'])])
	images = MultipleFileField('Upload images', validators=[FileAllowed(['jpg', 'png'])])
	submit = SubmitField('Post')
	

class CommentForm(FlaskForm):
	content = TextAreaField('Content', validators=[DataRequired()])
	submit = SubmitField('Comment')
	