from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
from myblogapp.models import Category
from wtforms.ext.sqlalchemy.fields import QuerySelectField

def enabled_categories():
    return Category.query.all()

class CategoryForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Add Category')

class PostForm(FlaskForm):
    category = QuerySelectField(query_factory=enabled_categories, allow_blank=True)
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Post Content', validators=[DataRequired()])
    img = FileField('Add Post Img', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Add Post')