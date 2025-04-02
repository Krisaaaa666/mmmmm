from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.http import HttpResponseNotFound
from django.contrib.auth import login

from django.shortcuts import render
from django.core.mail import send_mail
from .forms import FeedbackForm



def index(request):
    '''
    students = Student.objects.all() #строка которая определяет какие именно объекты мне нужно вывести из бд
    data ={
        'title': 'Главная страница'
    }'''
    return render(request,'main/index.html', #data,
                   # {'title':'Главная страница','students': students}  
                 ) #все что в фигурных скобках тоже относится к бд

def about(request):
    return render(request, 'main/about.html')

def postypauchim(request):
    return render(request, 'main/postypauchim.html')

def roditeli(request):
    return render(request, 'main/roditeli.html')

def registr(request):
    return render(request, 'main/registr.html')

def vxod(request):
    return render(request, 'main/vxod.html')

def contakt(request):
    return render(request, 'main/contakt.html')

def ychiteluam(request):
    return render(request, 'main/ychiteluam.html')

def akkaynt(request):
    return render(request, 'main/akkaynt.html')

def pravila(request):
    return render(request, 'main/pravila.html')

def handler404(request, exception):
    return HttpResponseNotFound(render(request, 'main/404.html'))

def registr(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            print("User created:", user.username)
            return redirect('vxod')  # Перенаправляем на страницу входа
    else:
        form = RegisterForm()

    return render(request, 'main/registr.html', {'form': form})

def vxod(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('akkaynt')  # Перенаправляем после успешного входа
    else:
        form = LoginForm()

    return render(request, 'main/vxod.html', {'form': form})





from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

def feedback_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Отправка email
        try:
            send_mail(
                f'Обратная связь от {name}',
                message,
                settings.DEFAULT_FROM_EMAIL,
                ['tovkalok17.08@mail.ru'],  # Почта, на которую будут отправляться сообщения
                fail_silently=False,
            )
            return render(request, 'contakt.html', {'success': True})
        except Exception as e:
            print(e)  # Логирование ошибки
            return render(request, 'contakt.html', {'error': True})

    return render(request, 'contakt.html')






