from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['UPLOAD_FOLDER'] = 'myblogapp/static/media'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from myblogapp.models import * 

from myblogapp.admin.routes import *
from myblogapp.user.routes import *
from myblogapp.blog.routes import *

app.register_blueprint(admin)
app.register_blueprint(user)
app.register_blueprint(blog)



