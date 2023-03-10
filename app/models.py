#from cop4521 import db
from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True) # auth0 id 
    email = db.Column(db.String(120), index=True, unique=True)
    #password_hash = db.Column(db.String(128)) # prob shouldnt be storing our passwords 
    def __repr__(self):
        return f'<User {self.id} {self.email} {self.username}>'

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_type = db.Column(db.String(140))
    by = db.Column(db.String(140))
    title = db.Column(db.String(140))
    url = db.Column(db.String(500))

    def __repr__(self):
        mydict = {
            "id":self.id,
            "post_type":self.post_type,
            "by":self.by,
            "title":self.title,
            "url":self.url
        }
        return str(mydict)

liked_posts = db.Table(
    "liked_posts",
    db.Column("user_id", db.ForeignKey(User.id), primary_key=True),
    db.Column("post_id", db.ForeignKey(Post.id), primary_key=True),
)

disliked_posts = db.Table(
    "disliked_posts",
    db.Column("user_id", db.ForeignKey(User.id), primary_key=True),
    db.Column("post_id", db.ForeignKey(Post.id), primary_key=True),
)

admins = db.Table(
    "admins",
    db.Column("user_id", db.ForeignKey(User.id), primary_key=True),
)
