from flask import render_template, redirect, url_for, Blueprint, request
from .forms import CategoryForm, PostForm
from myblogapp.models import Post, Category
from werkzeug.utils import secure_filename
import os
from myblogapp import app, db

blog = Blueprint('blog', __name__, template_folder='templates')

@blog.route('/admin/add-post', methods=['POST', 'GET'])
def post_add():
    form=PostForm()
    if form.validate_on_submit():
        file = request.files['img']
        post_img = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], post_img))

        new_post = Post(category=form.category.data, title=form.title.data, content=form.content.data, img=post_img)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('blog.post_add'))     
    return render_template('blog_post_add.html', form=form)

@blog.route('/admin/add-category', methods=['POST', 'GET'])
def cat_add():
    form=CategoryForm()
    cats=Category.query.all()
    if form.validate_on_submit():
        new_cat=Category(name=form.name.data)
        db.session.add(new_cat)
        db.session.commit()
        return redirect(url_for('blog.cat_add'))
    return render_template('blog_cat_add.html', form=form, cats=cats)

@blog.route('/admin/edit-category/<int:id>', methods=['POST', 'GET'])
def cat_edit(id):
    form=CategoryForm()
    selected_cat=Category.query.get(id)
    if request.method=='GET':
        form.name.data=selected_cat.name
    elif request.method=='POST':
        selected_cat.name=form.name.data
        db.session.commit()
        return redirect(url_for('blog.cat_add'))
    return render_template('blog_cat_add.html', form=form)


@blog.route('/admin/delete-category/<int:id>', methods=['POST', 'GET'])
def cat_delete(id):
    selected_cat=Category.query.get(id)
    db.session.delete(selected_cat)
    db.session.commit()
    return redirect(url_for('blog.cat_add'))

