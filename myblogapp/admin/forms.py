from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class SliderForm(FlaskForm):
    text = TextAreaField('Slider Text', validators=[DataRequired()])
    img = FileField('Add Slider Img', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Add Slider')