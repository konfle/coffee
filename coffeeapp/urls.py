from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('brewing.html/', views.brewing, name='brewing'),
    #path('post/<int:pk>/', views.post_detail, name='post_detail'),

]

