from django.shortcuts import render
from django.core.paginator import Paginator

def paginate(request, object_list, per_page=5):
    paginator= Paginator(object_list, per_page)
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
    } for idx in range(50)
]

def index(request):
    context = paginate(request, questions)
    return render(request, 'index.html', context=context)

def hot(request):
    context = paginate(request, questions)
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
    context = paginate(request, questions)
    context['string'] = string
    return render(request, 'question_by_tag.html', context=context)

def answer(request, pk):
    question = questions[pk]
    context = paginate(request, questions, 3)
    context['question'] = question
    return render(request, 'answer.html', context=context)

 