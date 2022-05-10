from flask import Blueprint
from flask import request, abort, redirect, render_template, url_for
from forms import PostForm
from questions_api import db
from utilties import get_last_saved_question_in_json, get_questions_by_part


bp = Blueprint('pages', __name__, template_folder='templates')


# функция обработчик json словарей, проверка правильности ключа, аборт на 404 при неверном ключе или типе значения.
@bp.route('/', methods=['POST'])
def get_questions_json():
    key, value = list(request.json.items())[0]
    print(request.json)
    if key == 'questions_num':
        try:
            questions_to_save = int(value)
        except ValueError:
            abort(404)
        get_questions_by_part(questions_to_save, db)
        return get_last_saved_question_in_json(db)
    else:
        abort(404)

#все то же самое, но с базовым фронтом.
@bp.route('/questions_form/', methods=['POST', 'GET'])
def get_questions():
     form = PostForm()
     if request.method == 'GET':
         return render_template('index.html', form=form)
     elif request.method == 'POST':
         questions_to_save = int(request.form['count'])
         get_questions_by_part(questions_to_save, db)
         return redirect(url_for('pages.last_object'))


@bp.route('/last-object')
def last_object():
    return get_last_saved_question_in_json(db)