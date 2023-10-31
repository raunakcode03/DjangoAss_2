from django.urls import path
from . import views

urlpatterns = [
    path('my_intro/', views.my_intro, name='my_intro'),
    path('my_work/', views.my_work, name='my_work'),
    path('assignment1/', views.assignment1, name='assignment1'),

]
