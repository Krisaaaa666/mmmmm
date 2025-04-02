from django import forms
from django.contrib.auth.forms import User, UserCreationForm, AuthenticationForm

class RegisterForm(UserCreationForm):
    lastname = forms.CharField(label='Фамилия', max_length=100)
    firstname = forms.CharField(label='Имя', max_length=100)
    middlename = forms.CharField(label='Отчество', max_length=100, required=False)
    email = forms.EmailField(label='Email')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'firstname', 'lastname', 'middlename']

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', max_length=100)
    password = forms.CharField(label='Пароль', max_length=100)

    class Meta:
        model = User
        fields = ['username', 'password']





class FeedbackForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=100)
    email = forms.EmailField(label='Email')
    message = forms.CharField(label='Сообщение', widget=forms.Textarea)


      