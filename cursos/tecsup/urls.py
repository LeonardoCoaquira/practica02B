from django.urls import path
from . import views

app_name = 'tecsup'

urlpatterns = [
    path('',views.index, name="index"),
    path('semestre/<int:semestre_id>/', views.semestre, name='semestre')
]