from django.urls import path
from . import views

app_name = 'coffeebeans'
urlpatterns = [
    path('', views.index, name='index'),
    path('brewing/', views.brewing, name='brewing'),
    path('roasting/', views.roasting, name='roasting'),
    path('grinding/', views.grinding, name='grinding'),
    path('drinks/', views.drinks, name='drinks'),
    path('survey/', views.survey, name='survey'),

    ]

