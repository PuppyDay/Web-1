from django.shortcuts import render

def index(request):
	return render(request, 'index.html', {})

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
