from django.shortcuts import render
from .models import Alunos
# Create your views here.

def registrar_alunos(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        Alunos.objects.create(nome=nome, email=email)
    return render(request, 'registrar_alunos.html')
