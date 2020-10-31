from django.shortcuts import render

questions = [
    {
        'id': idx,
        'title': f'{idx}. How to build a moon park?',
        'text': f'Guys, i have trouble with a moon park. Can\'t find the black-jack... It\'s text number {idx}!',
    } for idx in range(10)
]

tags = { 'tag_1':'bender', 
         'tag_2':'black-jack', 
         'tag_3':'perl', 
         'tag_4':'MySQL', 
         'tag_5':'django',
       }

def index(request):
	return render(request, 'index.html', {
        'questions': questions,
        'tags':tags,
    })

def add_question(request):
	return render(request, 'add_question.html', {
		'tags':tags,
		})

def registration(request):
	return render(request, 'registration.html', {
		'tags':tags,
		})

def log_in(request):
	return render(request, 'log_in.html', {
		'tags':tags,
		})

def profile(request):
	return render(request, 'profile.html', {
		'tags':tags,
		})

def question_by_tag(request, string):
	return render(request, 'question_by_tag.html', {
        'questions': questions,
        'tags':tags,
        'string':string,
	})

def answer(request, pk):
	question = questions[pk]
	return render(request, 'answer.html', {
        'question': question,
        'tags':tags,
	})
