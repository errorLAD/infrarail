from django.urls import path
from . import views

urlpatterns = [
    path('', views.cements, name='cements'),
    path('<int:id>', views.cement_detail, name='cement_detail'),
    path('cementsearch', views.cementsearch, name='cementsearch'),
]
