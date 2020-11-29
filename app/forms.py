from django import forms
from app.models import Article, Answer


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Login'}))
    password = forms.CharField(max_length=30,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


class SettingsForm(forms.Form):
    username = forms.CharField(max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Login'}))
    email = forms.EmailField(max_length=30,
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    nickname = forms.CharField(max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nickname'}))
    image = forms.ImageField(required=False,
                             widget=forms.FileInput(attrs={'class': "form-control-file file_ad"}))

    # TODO:обдумать случаи реального испльзования, какие могут быть фейлы


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Login'}))
    password = forms.CharField(max_length=30,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    # TODO: проверка пароля, уникальности логина?
    nickname = forms.CharField(max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nickname'}))
    email = forms.EmailField(max_length=30,
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    # TODO: дефолтная аватарка
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file file_ad'}))


class AddQuestionForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'text', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'How to build a moon park?'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Guys, i have trouble with a moon '
                                                                                  'park. Can\'t find the '
                                                                                  'black-jack...'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'})
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your answer here'}),
        }
