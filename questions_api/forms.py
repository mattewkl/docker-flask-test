from wtforms import validators, Form, IntegerField

class PostForm(Form):
    '''Форма числовая с валидацией по наличию хоть чего-то,
    и валидацей по величине числа.'''
    count = IntegerField('count',[validators.NumberRange(min=1, max=100000), validators.DataRequired()])




