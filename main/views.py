from django.shortcuts import render
from django.http import HttpResponse
from .models import User


def home(request):
    return HttpResponse("<h1>Привіт, світ!</h1>")


def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})
