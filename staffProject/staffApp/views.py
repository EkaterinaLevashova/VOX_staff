from django.shortcuts import render
from django.http import HttpResponse
from staffApp.models import *
from staffApp.forms import NewParticipantForm
from . import forms


# Create your views here.

def index(request):
    participants = AccessRecord.objects.all()
    form = NewParticipantForm()
    date_dict = {
        'participants': participants,
        'form': form,
    }

    if request.method == 'POST':
        form = NewParticipantForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            print('Success METAFORM ')
            return index(request)
        # else:
        #     print('ERROR FORM INVALID')

    return render(request, 'index.html', context=date_dict)


def game(request):
    return render(request, 'game.html')


def relative(request):
    form = forms.FormName()
    contex_dict = {
        'form': form,
        'text': "hello world",
        'number': 100,
    }

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print('VALIDATION SUCCEEDED!')
            print("NAME: " + form.cleaned_data['name'])
            print("EMAIL: " + form.cleaned_data['email'])
            print("TEXT: " + form.cleaned_data['text'])

    return render(request, 'relative-url.html', contex_dict)
