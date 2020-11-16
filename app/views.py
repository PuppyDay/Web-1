from django.shortcuts import render
from django.core.paginator import Paginator
from app.models import Article, User, Answer


def paginate(request, object_list, per_page=5):
    paginator = Paginator(object_list, per_page)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''
    context = {
        'questions': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url
    }
    return context


questions = [
    {
        'id': idx,
        'title': f'{idx}. How to build a moon park?',
        'text': f'Guys, i have trouble with a moon park. Can\'t find the black-jack... It\'s text number {idx}!',
        'likes': 10,
    } for idx in range(50)
]


def index(request):
    new_articles = Article.objects.sort_new()
    context = paginate(request, new_articles)
    return render(request, 'index.html', context=context)


def hot(request):
    hot_articles = Article.objects.sort_hot()
    context = paginate(request, hot_articles)
    return render(request, 'hot.html', context=context)


def add_question(request):
    return render(request, 'add_question.html', {})


def registration(request):
    return render(request, 'registration.html', {})


def log_in(request):
    return render(request, 'log_in.html', {})


def profile(request):
    return render(request, 'profile.html', {})


def question_by_tag(request, string):
    article_tag = Article.objects.sort_questions_by_tag(string)
    context = paginate(request, article_tag)
    context['string'] = string
    return render(request, 'question_by_tag.html', context=context)


def answer(request, pk):
    question = Article.objects.get(id=pk)
    all_answer = Answer.objects.question_answers(pk)
    context = paginate(request, all_answer, 3)
    context['question'] = question
    return render(request, 'answer.html', context=context)
