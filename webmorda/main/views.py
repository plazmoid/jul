from django.shortcuts import render, redirect
from main.models import *


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def contact(request):
    return render(request, 'main/contact.html')


def about_project(request):
    return render(request, 'main/about_project.html')


def test(request):
    return render(request, 'main/test.html')


def quiz(request, pagenum=None):
    # request.session["quiz"] хранит всю инфу о полученных ответах в виде
    # [answer, answer, answer, None, None, None]
    # где None означает ещё не полученный ответ

    # выставляем сессионную переменную
    if request.session.get("quiz") is None:
        cnt = QuizSelect.objects.count()
        request.session["quiz"] = [None] * cnt

    # POSTом отправляем результаты со страницы на сервер
    if request.method == "POST":
        # получаем выбранный элемент
        chosen = request.POST['selector']
        pagenum = int(pagenum)
        # фиксируем его в сессии
        request.session["quiz"][pagenum - 1] = chosen
        ctx = {"results": request.session["quiz"]}
        # дошли до последней страницы - показываем результаты
        if pagenum == len(ctx["results"]):
            return render(request, 'main/quiz_ready.html', context=ctx)
        # иначе редиректим на следующий опросник
        return redirect(f'/quiz/{pagenum + 1}')

    # просто нажали на кнопочку опросов
    if pagenum is None or pagenum == '':
        return redirect(f'/quiz/1')

    # получаем данные из БД для текущего опросника
    pagenum = int(pagenum)
    current_quiz = QuizSelect.objects.all()[pagenum - 1]
    current_quiz_data = QuizRules.objects.filter(
        page_name=current_quiz.internal_name
    )
    # фильтруем элементы для списка следующим образом:
    # если ни одного idшника из поля show_if не присутствует в массиве session["quiz"],
    # то не показываем элемент
    current_quiz_data = [
        d for d in current_quiz_data
        if d.show_if == '' or
        len(set(d.show_if.split(',')) & set(
            filter(None, request.session["quiz"]))) > 0
    ]

    quiz_data = {
        "name": current_quiz.name,
        "items": [{"id": d.item.id, "value": d.item.value} for d in current_quiz_data]
    }
    return render(request, 'main/quiz.html', context=quiz_data)
