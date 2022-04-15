from django.urls import path
from staffApp import views

app_name = 'staffApp'

urlpatterns = [
    path('relative', views.relative, name='relative'),
    path('game', views.game, name='game'),
    path('registration', views.registration, name='registration'),
    path('user_login', views.user_login, name='user_login'),
]
