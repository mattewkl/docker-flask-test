from questions_api import db

class Questions(db.Model):
    record_number = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.Integer, unique=True)
    question_text = db.Column(db.String(1000))
    answer = db.Column(db.String(1000))
    created = db.Column(db.DateTime)