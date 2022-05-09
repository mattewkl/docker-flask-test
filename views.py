import datetime
import json
import requests
from bs4 import BeautifulSoup as BS
from flask import Blueprint
from flask import render_template
from flask import request
from models import Questions
from forms import PostForm
from app import db
from sqlalchemy.exc import  IntegrityError

from flask import redirect, url_for

bp = Blueprint('pages', __name__, template_folder='templates')

# сделать функции для получения словарей, вынести в отдельный файл


@bp.route('/', methods=['POST', 'GET'])
def get_questions():
    form = PostForm()

    if request.method == 'POST':
        count = int(request.form['count'])
        chunks = count//100

        in_database_count = 0
        while count > 0:
            r = requests.get(f'https://jservice.io/api/random?count={count}').json()
            print(r)
            count -= count
            for element in r:
                id = element.get('id', 'API error, id not found')
                question_text = element.get('question', 'API error, questiontext not found')
                answer = element.get('answer', 'API error, answer not found')
                created = element.get('created_at', 'API error, creation date  not found')
                question = Questions(id=id, question_text=question_text, answer=answer, created=created)
                db.session.add(question)
                print(question)
                try:
                    db.session.commit()
                except IntegrityError:
                    print('Error')
                    db.session.rollback()
                    in_database_count += 1
        else:
            count += in_database_count

            # count -= count
            # soup = BS(r.content,'html.parser')
            # in_database_count = 0
            # for element in soup:
            #
            #     dict_string = str(element[1:-1])
            #     dict_list = dict_string.split(',{')
            #     for index in range(len(dict_list)):
            #         if index == 0:
            #             realdict = json.loads(dict_list[index])
            #             id, question_text, answer, created = realdict['id'], realdict['question'], realdict['answer'], realdict['created_at']
            #             question = Questions(id=id, question_text=question_text, answer=answer, created=created)
            #             db.session.add(question)
            #             try:
            #                 db.session.commit()
            #             except IntegrityError:
            #                 print('Error')
            #                 db.session.rollback()
            #                 in_database_count += 1
            #         else:
            #             realdict = json.loads('{'+dict_list[index])
            #             id, question_text, answer, created = realdict['id'], realdict['question'], realdict['answer'], realdict['created_at']
            #             question = Questions(id=id, question_text=question_text, answer=answer, created=created)
            #             db.session.add(question)


    return render_template('index.html', form=form)

