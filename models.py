from app import db

class Questions(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    question_text = db.Column(db.String(1000))
    answer = db.Column(db.String(1000))
    created = db.Column(db.DateTime)