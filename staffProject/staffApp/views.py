from django.shortcuts import render
from django.http import HttpResponse
from staffApp.models import *


# Create your views here.

def index(request):
    participants = AccessRecord.objects.all()
    date_dict = {'participants': participants}
    return render(request, 'index.html', context=date_dict)


def game(request):
    return render(request, 'game.html')


def relative(request):
    contex_dict = {'text': "hello world", 'number': 100}
    return render(request, 'relative-url.html', contex_dict)
