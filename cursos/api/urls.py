from django.urls import path,include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register(r'curso',views.CursoViewSet,basename='curso')

urlpatterns = [
    path('',views.IndexView.as_view()),
    path('semestres',views.SemestreView.as_view()),
    path('semestres/<int:semestre_id>',views.SemestreDetailView.as_view()),
    path('admin/',include(router.urls)),
    path('cursos/', views.CursoListView.as_view(), name='curso-list'),
    path('cursos/<int:curso_id>/', views.CursoDetailView.as_view(), name='curso-detail'),
]