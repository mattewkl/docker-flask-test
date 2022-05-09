from requests import get
from models import Questions
from sqlalchemy.exc import IntegrityError


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


def get_last_saved_question(db):
    return db.session.query(Questions).order_by(Questions.record_number.desc()).first()
