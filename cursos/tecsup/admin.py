from django.contrib import admin

# Register your models here.
from .models import Semestre, Curso

admin.site.register(Semestre)
admin.site.register(Curso)