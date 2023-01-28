from django.urls import path
from . import views

urlpatterns = [
    path('cementinquiry', views.cementinquiry, name='cementinquiry'),
]