from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import viewsets

from tecsup.models import Semestre, Curso
from .serializers import (
    SemestreSerializer,
    CursoSerializer
)

class IndexView(APIView):
    
    def get(self,request):
        lista_semestres = Semestre.objects.all()
        serializer_semestre = SemestreSerializer(lista_semestres,many=True)
        return Response(serializer_semestre.data)
    
class SemestreView(generics.ListCreateAPIView):
    queryset = Semestre.objects.all()
    serializer_class = SemestreSerializer
    
class SemestreDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Semestre.objects.all()
    lookup_url_kwarg  = 'semestre_id'
    serializer_class = SemestreSerializer
    
class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class CursoListView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class CursoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    lookup_url_kwarg = 'curso_id'
    serializer_class = CursoSerializer