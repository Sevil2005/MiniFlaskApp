from flask import render_template, redirect, url_for, Blueprint, request
from .forms import SliderForm
from myblogapp.models import Slider
from werkzeug.utils import secure_filename
import os
from myblogapp import app, db

admin = Blueprint('admin', __name__, template_folder='templates')

@admin.route('/admin')
def index():
    return render_template('admin_layout.html')

@admin.route('/admin/add-slider', methods=['POST', 'GET'])
def add_slider():
    form = SliderForm()
    if form.validate_on_submit():
        file = request.files['img']
        slider_img = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], slider_img))

        new_slider = Slider(text=form.text.data, img=slider_img)
        db.session.add(new_slider)
        db.session.commit()
        return redirect(url_for('user.index'))
    return render_template('admin_slider_add.html', form=form)