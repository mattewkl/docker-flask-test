from wtforms import validators, Form, IntegerField

class PostForm(Form):
    count = IntegerField('count',[validators.NumberRange(min=1, max=100000), validators.DataRequired()])




