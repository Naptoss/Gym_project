from django.urls import path
from . import views

urlpatterns = [
    path('registrar_alunos/', views.registrar_alunos, name='registrar_alunos'),
]
