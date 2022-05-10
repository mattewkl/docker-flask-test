from requests import get
from .models import Questions
from sqlalchemy.exc import IntegrityError
from flask import jsonify


def get_questions_in_json(count: int):
    return get(f'https://jservice.io/api/random?count={count}').json()


def update_questions_table(db, json_object) -> int:
    count = 0
    for element in json_object:
        question_id = element.get('id', 'API error, id not found')
        question_text = element.get('question', 'API error, question text not found')
        if not question_text:
            question_text = 'Empty string'
        answer = element.get('answer', 'API error, answer not found')
        if not answer:
            answer = 'Empty string'
        created = element.get('created_at', 'API error, creation date  not found')
        question = Questions(id=question_id, question_text=question_text, answer=answer, created=created)
        db.session.add(question)
        try:
            db.session.commit()
        except IntegrityError:
            print('Error')
            db.session.rollback()
            count += 1
    return count


def get_last_saved_question_in_json(db):
    last_saved_question = db.session.query(Questions).order_by(Questions.record_number.desc()).first()
    json_question = jsonify({
        'question_id': last_saved_question.id,
        'question_text': last_saved_question.question_text,
        'answer': last_saved_question.answer,
        'created': last_saved_question.created
    })
    json_question.status_code = 201
    return json_question

def get_questions_by_part(questions_to_save: int, db):
    while questions_to_save > 0:
        if questions_to_save > 100:
            json_object = get_questions_in_json(100)
            questions_to_save -= 100
        else:
            json_object = get_questions_in_json(questions_to_save)
            questions_to_save -= questions_to_save
        questions_not_added = update_questions_table(db, json_object)
        questions_to_save += questions_not_added