from app import db
from datetime import datetime
import enum


class Type(enum.Enum):
    news = 'news'
    publication = 'publication'
    other = 'other'


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    text = db.Column(db.String)
    image = db.Column(db.String, default='postdefault.jpg')
    created = db.Column(db.DateTime, default=datetime.now())
    type = db.Column(db.Enum(Type), default='news')
    enabled = db.Column(db.Boolean, default=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.image_file}', '{self.created}, '{self.type}')"
