from django.urls import path
from . import views
import playground

#URL Configuration
urlpatterns = [
    path('hello/', views.say_hello)
]
