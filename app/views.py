from django.shortcuts import render

questions = [
    {
        'id': idx,
        'title': f'{idx}. How to build a moon park?',
        'text': f'Guys, i have trouble with a moon park. Can\'t find the black-jack... It\'s text number {idx}!',
    } for idx in range(10)
]

def index(request):
	return render(request, 'index.html', {
        'questions': questions,
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
	return render(request, 'question_by_tag.html', {
        'questions': questions,
	})

def answer(request, pk):
	question = questions[pk]
	return render(request, 'answer.html', {
        'question': question
	})
