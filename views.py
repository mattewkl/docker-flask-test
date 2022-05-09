from flask import Blueprint
from flask import render_template
from flask import request
from forms import PostForm
from app import db
from utilties import  get_last_saved_question_in_json, get_questions_by_part
from flask import redirect, url_for, jsonify

bp = Blueprint('pages', __name__, template_folder='templates')


@bp.route('/', methods=['POST', 'GET'])
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
