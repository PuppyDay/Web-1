from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.paginator import Paginator
from app.models import *
from app.forms import *
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


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


@login_required
def add_question(request):
    if request.method == 'GET':
        form = AddQuestionForm()
    else:
        form = AddQuestionForm(data=request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user.profile
            question.save()
            question.tags.set(form.cleaned_data['tags'])
            return redirect(reverse('question', kwargs={'pk': question.id}))
    return render(request, 'add_question.html', {'form': form})       #TODO:создание своих тэгов


def registration(request):  # TODO:проверить всякое повторяющееся и корректность, дефолтная аватарка
    if request.method == 'GET':
        form = RegisterForm()
    else:
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],
                                            email=form.cleaned_data['email'],
                                            password=form.cleaned_data['password'])

            profile = Author.objects.create(user=user, name=form.cleaned_data['nickname'])
            if form.cleaned_data['image'] is not None:
                profile.image = form.cleaned_data['image']
                profile.save()

            auth.login(request, user)
            # return redirect('/')
    return render(request, 'registration.html', {'form': form})


def log_in(request):
    if request.method == 'GET':
        request.session['next'] = request.GET.get('next', '/')
        form = LoginForm()
    # path = request.GET.get('next')
    else:
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = auth.authenticate(request, **form.cleaned_data)
            if user is not None:
                auth.login(request, user)
                return redirect(request.session.pop('next'))
    return render(request, 'log_in.html', {'form': form})


def logout(request):
    auth.logout(request)
    return redirect('/')  # TODO: куда должен быть?


@login_required
def profile(request):
    if request.method == 'GET':
        form = SettingsForm(initial={"username": request.user.username,
                                     "email": request.user.email,
                                     "nickname": request.user.profile.name})
    else:
        form = SettingsForm(request.POST, request.FILES, initial={"username": request.user.username,
                                                                  "email": request.user.email,
                                                                  "nickname": request.user.profile.name})
        if form.is_valid():
            user = request.user
            profile = user.profile
            if 'username' in form.changed_data:
                user.username = form.cleaned_data['username']
            if 'email' in form.changed_data:
                user.email = form.cleaned_data['email']
            if 'nickname' in form.changed_data:
                profile.name = form.cleaned_data['nickname']
            if 'image' in form.changed_data:
                profile.image = form.cleaned_data['image']
            profile.save()
            user.save()
        else:
            pass

    return render(request, 'profile.html', {'form': form})
    # TODO:сделать для чего лейблы,маил проверка, пароль, при загрузке кинка показывалась, фото чтоб удалялось из папки


def question_by_tag(request, string):
    article_tag = Article.objects.sort_questions_by_tag(string)
    context = paginate(request, article_tag)
    context['string'] = string
    return render(request, 'question_by_tag.html', context=context)


def answer(request, pk):
    question = get_object_or_404(Article, id=pk)
    all_answer = Answer.objects.question_answers(pk)
    context = paginate(request, all_answer, 3)
    context['question'] = question
    if request.method == 'GET':
        form = AnswerForm()
    else:
        form = AnswerForm(data=request.POST)
        if form.is_valid():
            ans = form.save(commit=False)
            ans.author = request.user.profile
            ans.question = question
            ans.save()
            all_ans = context['questions'].paginator.count
            return redirect(reverse('question', kwargs={'pk': question.id}) + f'?page={int(all_ans / 3) +1}')

    context['form'] = form
    return render(request, 'answer.html', context=context)
    # TODO:сделать для красоты регулированеи в html

