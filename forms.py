from wtforms import validators, Form, IntegerField, StringField

class PostForm(Form):
    count = IntegerField('count',[validators.Length(min=1, max=4)])

# class QuesionForm(Form):
#     id = IntegerField('id')
#     question_text = StringField('question_text')
#     answer = StringField('answer')


