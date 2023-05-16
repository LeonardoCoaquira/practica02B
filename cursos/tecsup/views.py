from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    curso_list = Curso.objects.order_by('titulo')[:6]
    semestre_list = Semestre.objects.all()
    context = {
        'cursos':curso_list,
        'semestres': semestre_list
    }
    return render(request,'index.html',context)

def semestre(request, semestre_id):
    semestre = Semestre.objects.get(pk=semestre_id)
    lista_cursos = semestre.curso_set.all()
    lista_semestres = Semestre.objects.all()

    context = {
        'cursos':lista_cursos,
        'semestres':lista_semestres,
        'semestre':semestre
    }
    
    return render(request,'index.html',context)