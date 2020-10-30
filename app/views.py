from django.shortcuts import render

questions = [
    {
        'id': idx,
        'title': 'title{idx}',
        'text': 'text text',
    } for idx in range(10)
]

def index(request):
	return render(request, 'index.html', {
		'questions':questions,
		})

def add_question(request):
	return render(request, 'add_question.html', {})

def registration(request):
	return render(request, 'registration.html', {})

def log_in(request):
	return render(request, 'log_in.html', {})

def profile(request):
	return render(request, 'profile.html', {})

def question_by_tag(request):
	return render(request, 'question_by_tag.html', {})

def answer(request):
	return render(request, 'answer.html', {})
