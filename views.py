from flask import Blueprint
from flask import render_template
from flask import request
from forms import PostForm
from app import db
from utilties import get_questions_in_json, update_questions_table, get_last_saved_question
from flask import redirect, url_for

bp = Blueprint('pages', __name__, template_folder='templates')


@bp.route('/', methods=['POST', 'GET'])
def get_questions():
    form = PostForm()
    if request.method == 'GET':
        return render_template('index.html', form=form)
    elif request.method == 'POST':
        questions_to_save = int(request.form['count'])
        while questions_to_save > 0:
            if questions_to_save > 100:
                json_object = get_questions_in_json(100)
                questions_to_save -= 100
            else:
                json_object = get_questions_in_json(questions_to_save)
                questions_to_save -= questions_to_save
            questions_not_added = update_questions_table(db, json_object)
            questions_to_save += questions_not_added
        return redirect(url_for('pages.last_object'))


@bp.route('/last-object')
def last_object():
    last_saved_question = get_last_saved_question(db)
    return render_template('last-object.html', record=last_saved_question)
