from django.shortcuts import render
from.models import Student


def akkaynt(request):
    accounts = Student.objects.all()
    return render(request, 'main/akkaynt.html',
{'accounts': accounts}) 

