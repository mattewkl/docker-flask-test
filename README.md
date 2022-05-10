# docker-flask-test

Примечание:
Уважаемые работодатели, readme написан в том числе на случай, если кто-то захочет покопаться в этом коде кроме вас. Прошу понять подробность и количество ссылок.
Тестовое задание.

0 - устанавливаем свежий докер. Windows - https://docs.docker.com/desktop/windows/install/
Линуксы - https://docs.docker.com/desktop/linux/install/
0.1 - Устанавливаем Python 3.8 
0.2 - Устанавливаем гит.

1) Клонируем репозиторий. Создаем новую директорию, в консоли в этой директории делаем git init, затем git-clone -r https://github.com/mattewkl/docker-flask-test.git
2) В консоли пишем docker-compose up
3) создаем виртуальное окружение, активируем его, устанавливаем библиотеки указанные в requirements.txt Гайд по настройке виртуального окружения: https://python-scripts.com/virtualenv
4) в корневой папке проекта flask db init
5) flask db migrate 'название миграции'
6) flask db upgrade
7) python manage.py
8) вы великолепны, сервер запущен. Теперь - к запросам.

Реализовано два способа выполнения этого добра - через базовый фрон, или через отправку пост запросов напрямую.
Через фронт - заходите на localhost:5000/questions_form/, пишите в форме количество вопросов.
Через консоль(тесты проводились в Chrome)
:
fetch('http://127.0.0.1:5000/', {
  method: 'POST',
  body: JSON.stringify({
 "questions_num": 100#или любое число какое вам нравится
}),
  headers: {
    'Content-type': 'application/json; charset=UTF-8'
  }
})
.then(res => res.json())
.then(console.log)

Работает API стабильно, обрабатывало спокойно по 10-15 тысяч вопросов за раз.
