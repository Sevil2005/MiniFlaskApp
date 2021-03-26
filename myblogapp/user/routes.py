from flask import render_template, redirect, url_for, Blueprint
from myblogapp.models import Slider

user = Blueprint('user', __name__, template_folder='templates')

@user.route('/')
def index():
    sliders = Slider.query.all()
    return render_template('user_index.html',sliders=sliders)