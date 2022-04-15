from django.shortcuts import render
from . import forms
from staffApp.models import *
from staffApp.forms import *
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


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
    form = FormName()
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


def registration(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    context_dict = {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered,
    }
    return render(request, 'registration.html', context=context_dict)


@login_required
def special(request):
    return HttpResponse("U are login, nice!")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:

            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone try to login and failed!")
            print("Username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details supplied")
    else:
        return render(request, 'login.html', {})
