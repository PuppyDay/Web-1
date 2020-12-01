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
    repeat_password = forms.CharField(max_length=30,
                                      widget=forms.PasswordInput(
                                          attrs={'class': 'form-control', 'placeholder': 'Repeat password'}))
    # TODO: проверка пароля, уникальности логина?
    nickname = forms.CharField(max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nickname'}))
    email = forms.EmailField(max_length=30,
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    # TODO: дефолтная аватарка
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file file_ad'}))

    def clean_repeat_password(self):
        cleaned_data = super(RegisterForm, self).clean()

        password = cleaned_data['password']
        repeat_password = cleaned_data['repeat_password']
        if password and repeat_password and password != repeat_password:
            raise forms.ValidationError('Passwords do not match! Please, try again')
        return cleaned_data

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        if cleaned_data:
            raise forms.ValidationError('Registration error')
        return cleaned_data



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
# TODO:од клин?
