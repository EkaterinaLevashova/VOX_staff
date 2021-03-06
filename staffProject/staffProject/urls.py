from django.contrib import admin
from staffApp import views
from django.urls import path
from django.conf.urls import include


urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('staffApp/', include('staffApp.urls')),
    path('logout/', views.user_logout, name='logout'),
    path('special/', views.special, name='special'),
    # path("__reload__/", include("django_browser_reload.urls")),
]
