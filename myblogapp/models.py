from myblogapp import db

class Slider(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    img = db.Column(db.String(20))

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    posts = db.relationship('Post', backref='category', lazy=True)

    def __str__(self):
        return self.name

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    content = db.Column(db.Text)
    img = db.Column(db.String(20))
    category_id = db.Column(db.ForeignKey('category.id'))